#!/bin/bash
# QX-01: Run full evaluation pipeline
# Usage: bash scripts/run_evaluation.sh

echo "=== QX-01 Evaluation Pipeline ==="
python src/evaluate.py
python src/count_violations.py
python src/resilience_sim.py
python src/visualise.py
echo "Evaluation complete. Check results/ and figures/ directories."
