# QX-01 Physics-Informed Machine Learning for Solar Microgrid Resilience of Healthcare Facilities

**A Stochastic Study of the Sylhet Monsoon Corridor, Bangladesh**

[![License: MIT](https://img.shields.io/badge/License-MIT-teal.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.x-orange.svg)](https://pytorch.org)
[![arXiv](https://img.shields.io/badge/arXiv-preprint-red.svg)](https://arxiv.org)

---

## Overview

This repository contains the complete implementation, data pipeline, trained models,
and reproducible results for the research paper:

> **Prosun Datta**, "Physics-Informed Machine Learning for Solar Microgrid Resilience
> of Healthcare Facilities: A Stochastic Study of the Sylhet Monsoon Corridor,
> Bangladesh."
> arXiv preprint: [link to be added upon submission]

### Core Contribution

A custom physics-informed loss function with three penalty terms embedded into a
deep recurrent neural network for solar power forecasting:

```
L_total = L_MSE + λ₁·L_max + λ₂·L_night + λ₃·L_monsoon
```

- **L_max** — upper-bound constraint (Shockley-Queisser physical limit)
- **L_night** — nocturnal zero constraint (no power when sun is below horizon)
- **L_monsoon** — novel dual rain-cooling and moisture-attenuation term (first in literature)

---

## Repository Structure

```
qx-01-piml-solar-sylhet/
│
├── data/
│   ├── raw/                    # Raw NASA POWER download (CSV)
│   ├── processed/              # Cleaned features + train/val/test arrays
│   └── external/               # Any third-party reference data
│
├── src/                        # All production source code
│   ├── data_loader.py          # Load and clean NASA POWER data
│   ├── features.py             # Full feature engineering pipeline
│   ├── pvlib_sim.py            # PVLib PV power simulation
│   ├── dataset.py              # Sliding-window sequences + splits
│   ├── models.py               # LSTM, GRU, and PIML-LSTM classes
│   ├── physics_loss.py         # L_max, L_night, L_monsoon loss terms
│   ├── train.py                # Training loop with early stopping
│   ├── evaluate.py             # RMSE, MAE, R², seasonal metrics
│   ├── count_violations.py     # Physics violation counter
│   ├── resilience_sim.py       # Microgrid simulation (LOLP, EENS, CLSR)
│   ├── load_model.py           # Synthetic UHC load profile generator
│   ├── visualise.py            # All publication-quality figures
│   └── utils.py                # Shared utility functions
│
├── notebooks/                  # Jupyter notebooks (exploration + dev)
│   ├── 01_data_exploration.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_pvlib_simulation.ipynb
│   ├── 04_baseline_models.ipynb
│   ├── 05_physics_loss_dev.ipynb
│   ├── 06_piml_model.ipynb
│   ├── 07_ablation_study.ipynb
│   ├── 08_resilience_simulation.ipynb
│   └── 09_results_figures.ipynb
│
├── models/
│   ├── lstm_baseline.pt        # Saved LSTM baseline weights
│   ├── gru_baseline.pt         # Saved GRU baseline weights
│   ├── piml_best.pt            # Saved best PIML model weights
│   └── checkpoints/            # Intermediate training checkpoints
│
├── results/
│   ├── metrics/                # CSV metric tables (RMSE, MAE, R²)
│   ├── resilience/             # LOLP, EENS, CLSR results
│   └── ablation/               # Ablation study results
│
├── figures/                    # All paper figures (PNG, 300 DPI)
│   ├── forecasting/
│   ├── resilience/
│   └── features/
│
├── configs/
│   ├── data_config.json        # Data paths and parameters
│   ├── model_config.json       # Model architecture parameters
│   ├── piml_config.json        # Best lambda values (hyperparameters)
│   └── sim_config.json         # Resilience simulation parameters
│
├── tests/                      # Unit tests for all modules
├── scripts/                    # Automation scripts
├── docs/                       # Extended methodology notes
├── paper/                      # LaTeX source (Overleaf export)
├── requirements.txt            # All package versions (pinned)
├── setup.py
├── LICENSE                     # MIT License
└── README.md
```

---

## Quickstart — Reproduce All Results

### 1. Clone the repository
```bash
git clone https://github.com/prosunkdatta/qx-01-piml-solar-sylhet.git
cd qx-01-piml-solar-sylhet
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Download NASA POWER data
```bash
python scripts/download_nasa_power.py
```
This downloads 20 years (2005–2024) of hourly weather data for Sylhet
(24.89°N, 91.87°E) directly from the NASA POWER API.

### 4. Run the full data pipeline
```bash
python src/data_loader.py
python src/features.py
python src/pvlib_sim.py
python src/dataset.py
```

### 5. Train all models
```bash
bash scripts/run_training.sh
```

### 6. Evaluate and generate figures
```bash
bash scripts/run_evaluation.sh
```

All figures will be saved to `figures/` and all metrics to `results/`.

---

## Data

- **Source:** [NASA POWER](https://power.larc.nasa.gov/) — Prediction of
  Worldwide Energy Resources
- **Location:** Sylhet, Bangladesh (24.89°N, 91.87°E)
- **Period:** 2005–2024 (20 years, hourly resolution)
- **Variables:** GHI, T2M, RH2M, PRECTOTCORR, WS10M, CLRSKY_SFC_SW_DWN
- **PV simulation:** PVLib ModelChain, 1 kW monocrystalline Si panel,
  η = 20%, A = 5 m², γ = −0.004/°C, 23° tilt

---

## Models

| Model | Description | Loss |
|-------|-------------|------|
| LSTM Baseline | 2-layer LSTM, 64 units, dropout 0.2 | MSE |
| GRU Baseline | 2-layer GRU, 64 units, dropout 0.2 | MSE |
| PVLib Deterministic | Physics model, no ML | — |
| PIML-LSTM (ours) | Same LSTM + physics loss | L_MSE + λ₁L_max + λ₂L_night + λ₃L_monsoon |

---

## Resilience Metrics

| Metric | Full Name | Description |
|--------|-----------|-------------|
| LOLP | Loss of Load Probability | Fraction of hours supply < demand |
| EENS | Expected Energy Not Served | Total kWh unserved to critical loads |
| CLSR | Critical Load Survival Rate | Fraction of time Tier-1 loads fully served |

---

## Citation

If you use this code or data in your research, please cite:

```bibtex
@article{prosun2027piml,
  title   = {Physics-Informed Machine Learning for Solar Microgrid Resilience
             of Healthcare Facilities: A Stochastic Study of the Sylhet
             Monsoon Corridor, Bangladesh},
  author  = {Prosun, Datta},
  journal = {IEEE Transactions on Sustainable Energy},
  year    = {2027},
  note    = {Under review. arXiv preprint available.}
}
```

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
All code, data, and models are released openly in the spirit of reproducible science.

---

## Contact

**Prosun Datta**
prosunkdatta@gmail.com |
[LinkedIn](https://linkedin.com/in/prosunkdatta) |
[GitHub](https://github.com/prosunkdatta)

*Prosun Datta — Physics-Informed Intelligence Systems Research*
