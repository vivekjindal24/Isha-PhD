# Smart Farming WSN: Cooling-Aware Optimization

This repository contains the research project on **Cooling-Aware Clustered Sleep-Wake Optimization for Heterogeneous Smart Farming Wireless Sensor Networks (WSNs)**.

## 📂 Repository Structure

```
.
├── sleep_wake_coverage_optimization.ipynb  # Main simulation notebook
├── latex/                                   # LaTeX manuscript (ready for Overleaf)
│   ├── main.tex                            # Master LaTeX file
│   ├── sections/                           # Individual content sections
│   ├── scripts/                            # Figure & table generation
│   ├── references.bib                      # Bibliography
│   └── README_LaTeX.md                     # LaTeX build instructions
├── figures/                                 # Generated figures (600 dpi)
├── export_docx.py                          # Initial DOCX generation script
├── build_revised_docx.py                   # Enhanced DOCX with appendices
├── SmartFarming_CoolingPeriod_Minimization.docx
└── SmartFarming_Revised_Manuscript.docx
```

## 🎯 Key Features

- **Cooling-Aware CH Selection**: Multi-criteria cluster head selection with explicit cooling penalty
- **Routing Optimization**: Modified Dijkstra avoiding nodes in cooling state
- **Sleep-Wake Coverage**: Redundancy-driven scheduling with adaptive sensing radius
- **Regional Partitioning**: Five-region spatial division for stability

## 📊 Results Highlights

- **+80%** network lifetime vs LEACH
- **+31%** energy efficiency
- **+27.4%** coverage maintenance
- **-44.4%** per-round energy usage
- **~68%** cooling overhead reduction
- **0.973** packet delivery ratio

## 🚀 Quick Start

### Simulation
Open `sleep_wake_coverage_optimization.ipynb` in Jupyter:
```bash
jupyter notebook sleep_wake_coverage_optimization.ipynb
```

### LaTeX Manuscript
Upload the `latex/` directory to Overleaf or compile locally:
```bash
cd latex
latexmk -pdf main.tex
```

### Generate Figures (≥600 dpi)
```bash
python latex/scripts/export_figures.py --metrics metrics.json --out latex/figures
```

### Generate Tables with CI
```bash
python latex/scripts/generate_tables.py --samples metrics_samples.json --out latex/sections/ablation_auto.tex
```

## 📝 Publications

Manuscript ready for submission to SCI-indexed journals in WSN/IoT domains.

## 🛠 Requirements

- Python 3.8+
- Jupyter Notebook
- matplotlib, numpy, scipy
- python-docx (for DOCX generation)
- LaTeX distribution (TeX Live or MikTeX)

## 📄 License

[Add your license here]

## 👥 Authors

[Add author information]

## 📧 Contact

[Add contact information]

---

**Note**: This is a research project. Figures and tables are generated from simulation outputs. See `latex/README_LaTeX.md` for detailed build instructions.
