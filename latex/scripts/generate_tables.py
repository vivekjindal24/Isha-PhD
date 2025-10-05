"""Generate LaTeX tables with mean ± 95% CI from metric samples.
Input metrics_samples.json structure example:
{
  "ablation": {
    "full": {"lifetime": [...], "energy_per_round": [...], "coverage": [...], "pdr": [...]},
    "no_cooling": {...},
    ...
  }
}
Outputs tables fragment to stdout or --out file.
"""
import json, argparse, math, statistics as stats
from pathlib import Path

CONF_Z = 1.96  # 95% normal approximation

ORDER = [
    ("Full Model", "full"),
    ("No Cooling Penalty", "no_cooling"),
    ("No Sleep--Wake", "no_sleep"),
    ("No Radius Adaptation", "no_radius"),
    ("Baseline (LEACH)", "baseline"),
]

FIELDS = [
    ("lifetime", "Lifetime"),
    ("energy_per_round", "Energy/round"),
    ("coverage", "Coverage"),
    ("pdr", "PDR"),
]

def mean_ci(arr):
    if not arr:
        return ("--", "--")
    m = stats.mean(arr)
    if len(arr) > 1:
        sd = stats.pstdev(arr)  # population stdev; can swap to stdev
        ci = CONF_Z * sd / math.sqrt(len(arr))
    else:
        ci = 0.0
    return m, ci


def format_val(m, ci, precision=4):
    if m == "--":
        return "--"
    return f"{m:.{precision}f} $\\pm$ {ci:.{precision}f}"


def build_table(data):
    lines = []
    header = ("Variant & " + " & ".join(lbl for _, lbl in FIELDS) + r" \\" )
    lines.append(r"\begin{tabular}{@{}lcccc@{}}")
    lines.append(r"\toprule")
    lines.append(header)
    lines.append(r"\midrule")
    for variant_name, key in ORDER:
        metrics = data.get(key, {})
        cells = [variant_name]
        for field_key, _ in FIELDS:
            m, ci = mean_ci(metrics.get(field_key, []))
            prec = 0 if field_key == "lifetime" else 4 if field_key == "energy_per_round" else 1 if field_key == "coverage" else 3
            cells.append(format_val(m, ci, precision=prec))
    # Each table row ends with LaTeX line break \\
    lines.append(" & ".join(cells) + r" \\ ")
    lines.append(r"\bottomrule")
    lines.append(r"\end{tabular}")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--samples", required=True, help="metrics_samples.json path")
    ap.add_argument("--out", help="Optional output .tex file")
    args = ap.parse_args()

    with open(args.samples) as f:
        blob = json.load(f)
    ablation = blob.get("ablation", {})
    table_tex = build_table(ablation)

    caption = r"% Auto-generated ablation table with 95\% CI\n" \
              r"\begin{table}[ht]\n\centering\n" \
              r"\caption{Ablation of architectural components (mean $\pm$ 95\% CI).}" \
              "\n" + table_tex + "\n" + r"\label{tab:ablation-auto}\n\end{table}\n"

    if args.out:
        Path(args.out).write_text(caption)
        print(f"Wrote {args.out}")
    else:
        print(caption)

if __name__ == "__main__":
    main()
