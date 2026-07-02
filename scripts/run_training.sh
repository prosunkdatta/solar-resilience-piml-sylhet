#!/bin/bash
# Run full training pipeline
# Usage: bash scripts/run_training.sh

echo "=== Training Pipeline ==="
echo "Step 1: Data pipeline"
python src/data_loader.py
python src/features.py
python src/pvlib_sim.py
python src/dataset.py

echo "Step 2: Train baselines"
python src/train.py --model lstm_baseline
python src/train.py --model gru_baseline

echo "Step 3: Train PIML model (ablation variants)"
python src/train.py --model piml --variant 1
python src/train.py --model piml --variant 2
python src/train.py --model piml --variant 3
python src/train.py --model piml --variant 4

echo "Training complete."
