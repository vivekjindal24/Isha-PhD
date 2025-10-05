# LaTeX Production Package

This package is ready for Overleaf: upload the entire `latex/` directory contents. Missing figures (placeholders) can be added later; compilation will succeed if you comment out absent figure includes.

## 1. Contents
- `main.tex` master file with section includes
- `sections/` individual content files (abstract, introduction, methodology, results, limitations, conclusion, algorithms, tables, appendix)
- `scripts/` Python utilities to regenerate figures and tables
- `references.bib` BibTeX skeleton
- `figures/` (initially empty; populate with generated PDFs/PNGs)

## 2. Build
Latexmk (recommended):
```
latexmk -pdf -interaction=nonstopmode main.tex
```
Manual sequence:
```
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```
On Overleaf this sequence is automated; just press Recompile.

## 3. Figure Regeneration
1. Export metrics to `metrics.json`.
2. Generate figures:
```
python scripts/export_figures.py --metrics metrics.json --out figures
```
Outputs 600 dpi PNG + PDF (vector) for journal submission.

## 4. Ablation Table (Mean ± 95% CI)
Create `metrics_samples.json` with arrays per variant; then:
```
python scripts/generate_tables.py --samples metrics_samples.json --out sections/ablation_auto.tex
```
Add `\input{sections/ablation_auto}` to `main.tex` (or replace static table in `tables.tex`).

## 5. Parameter Sweeps
Implement sweeps in a future `scripts/parameter_sweeps.py` producing:
```
figures/sweep_delta.pdf
figures/sweep_fmax.pdf
figures/sweep_tau.pdf
```
Referenced in `appendix.tex`.

## 6. Cross-Referencing
Labels:
- Algorithms: `alg:ch-selection`, `alg:routing`, `alg:sleep-wake`
- Tables: `tab:parameters`, `tab:ablation`, `tab:ablation-auto`
- Figures: `fig:sweep-delta`, `fig:sweep-fmax`, `fig:sweep-tau`

Use: `\cref{alg:ch-selection}` etc.

## 7. Switching to `algorithm2e`
Replace:
```
\usepackage{algorithm}
\usepackage{algpseudocode}
```
with:
```
\usepackage[ruled,vlined]{algorithm2e}
```
Then adapt syntax (e.g. `\For{ }` blocks). Either style is acceptable for Overleaf.

## 8. Troubleshooting
| Symptom | Cause | Fix |
|---------|-------|-----|
| Missing figure file | Not yet generated | Run export script or comment out `\includegraphics` |
| Citation shows [?] | Bib not processed yet | Recompile twice / ensure key in `references.bib` |
| Package not found (local) | Incomplete TeX install | Install full TeX Live / MikTeX; Overleaf already has it |
| Algorithm float out of place | Float placement constraints | Add `[H]` with `\usepackage{float}` or rearrange |
| Overfull hbox warnings | Long inline math or URLs | Use `\url{}` or add discretionary breaks |

## 9. Bibliography
Current style: `IEEEtran`. Change via `\bibliographystyle{...}`. Add DOIs or URLs for final submission.

## 10. Metadata / Compliance
Add ORCIDs, funding, conflicts via `\author` footnotes or a pre-`\bibliographystyle` section. For structured data availability, create a `\section*{Data Availability}`.

## 11. Cleaning
```
latexmk -C
```
removes auxiliary outputs. Overleaf handles this automatically.

## 12. Next Steps
- Populate authors and affiliations
- Add extended related work if journal requires
- Generate real sweep plots
- Expand references for final submission

---
Ready for upload: copy everything under `latex/` into Overleaf root. Generate figures before final compile to avoid placeholder warnings.
