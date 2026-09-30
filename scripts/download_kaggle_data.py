"""Download the Kaggle datasets configured for CareerCraft AI.

Prerequisite: authenticate the Kaggle CLI (`kagglehub` or `kaggle.json`).
This script only downloads data; it does not upload anything to Kaggle.
"""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "raw" / "kaggle"
DATASETS = [
    ("snehaanbhawal/resume-dataset", OUT / "resume_dataset"),
    ("keerthiramesh470/resume-skill-gap-analyzer-dataset", OUT / "skill_gap_dataset"),
]


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for dataset, destination in DATASETS:
        destination.mkdir(parents=True, exist_ok=True)
        print(f"Downloading {dataset} -> {destination}")
        cmd = [
            sys.executable, "-m", "kaggle", "datasets", "download",
            "-d", dataset, "-p", str(destination), "--unzip"
        ]
        subprocess.run(cmd, check=True)
    print("\nKaggle downloads complete.")


if __name__ == "__main__":
    main()
