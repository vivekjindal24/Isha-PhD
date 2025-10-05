"""Export performance curves at high resolution (>=600 dpi) as PNG and PDF.
Assumes a metrics JSON file with per-round arrays, e.g.:
{
  "round": [1,2,...],
  "lifetime_active_nodes": [...],
  "energy_per_round": {"ours": [...], "leach": [...], ...},
  "coverage": {"ours": [...], "leach": [...], ...},
  "pdr": {"ours": [...], "leach": [...], ...}
}
"""
import json, os, argparse
from pathlib import Path
import matplotlib.pyplot as plt
plt.rcParams.update({"pdf.fonttype":42, "ps.fonttype":42, "font.size":10})

PALETTE = ["#1b9e77","#d95f02","#7570b3","#e7298a","#66a61e","#e6ab02"]


def _ensure_dir(p: Path):
    p.mkdir(parents=True, exist_ok=True)


def plot_metric(rounds, data_map, ylabel, fname, legend_loc="best"):
    fig, ax = plt.subplots(figsize=(3.5,2.4), dpi=300)  # base DPI; we'll also export higher
    for idx, (label, series) in enumerate(data_map.items()):
        ax.plot(rounds, series, label=label, lw=1.4, color=PALETTE[idx % len(PALETTE)])
    ax.set_xlabel("Round")
    ax.set_ylabel(ylabel)
    ax.grid(alpha=0.3)
    ax.legend(loc=legend_loc, fontsize=8)
    fig.tight_layout()
    fig.savefig(fname.with_suffix('.png'), dpi=600)
    fig.savefig(fname.with_suffix('.pdf'))
    plt.close(fig)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--metrics", required=True, help="Path to metrics JSON")
    ap.add_argument("--out", default="../figures", help="Output directory for figures")
    args = ap.parse_args()

    metrics_path = Path(args.metrics)
    out_dir = Path(args.out)
    _ensure_dir(out_dir)

    with open(metrics_path) as f:
        metrics = json.load(f)

    rounds = metrics.get("round") or list(range(1, len(next(iter(metrics.get("coverage", {}).values()), [])) + 1))

    if "energy_per_round" in metrics:
        plot_metric(rounds, metrics["energy_per_round"], "Energy / round (J)", out_dir / "energy_per_round")
    if "coverage" in metrics:
        plot_metric(rounds, metrics["coverage"], "Coverage (%)", out_dir / "coverage")
    if "pdr" in metrics:
        plot_metric(rounds, metrics["pdr"], "PDR", out_dir / "pdr")
    if "lifetime_active_nodes" in metrics:
        plot_metric(rounds, {"Active Nodes": metrics["lifetime_active_nodes"]}, "Active Nodes", out_dir / "active_nodes")

    print(f"Figures written to {out_dir.resolve()}")

if __name__ == "__main__":
    main()
