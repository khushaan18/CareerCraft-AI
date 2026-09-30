from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from evaluation.evaluator import run, dataset_status

if __name__ == "__main__":
    print(json.dumps({"metrics": run(), "datasets": dataset_status()}, indent=2))
