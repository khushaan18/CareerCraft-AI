import csv, json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data' / 'evaluation' / 'resume_job_evaluation.csv'


def run():
    rows = list(csv.DictReader(DATA.open(encoding='utf-8')))
    exact = 0
    scores = []
    for r in rows:
        req = {x.strip().lower() for x in r['required_skills'].split('|') if x.strip()}
        have = {x.strip().lower() for x in r['resume_skills'].split('|') if x.strip()}
        overlap = len(req & have) / max(1, len(req))
        pred = 'fit' if overlap >= 0.8 else ('potential' if overlap >= 0.4 else 'not_fit')
        exact += pred == r['expected_label']
        scores.append(overlap)
    return {
        'examples': len(rows),
        'label_accuracy': round(exact / max(1, len(rows)), 4),
        'mean_required_skill_coverage': round(sum(scores) / max(1, len(scores)), 4),
    }


def dataset_status():
    kaggle_root = ROOT / 'data' / 'raw' / 'kaggle'
    return {
        'resume_dataset_downloaded': (kaggle_root / 'resume_dataset').exists() and any((kaggle_root / 'resume_dataset').iterdir()),
        'skill_gap_dataset_downloaded': (kaggle_root / 'skill_gap_dataset').exists() and any((kaggle_root / 'skill_gap_dataset').iterdir()),
        'benchmark_examples': sum(1 for _ in csv.DictReader(DATA.open(encoding='utf-8'))),
    }


if __name__ == '__main__':
    print(json.dumps({'metrics': run(), 'datasets': dataset_status()}, indent=2))
