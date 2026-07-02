#!/bin/bash
# Run full evaluation pipeline
# Usage: bash scripts/run_evaluation.sh

echo "=== Evaluation Pipeline ==="
python src/evaluate.py
python src/count_violations.py
python src/resilience_sim.py
python src/visualise.py
echo "Evaluation complete. Check results/ and figures/ directories."
