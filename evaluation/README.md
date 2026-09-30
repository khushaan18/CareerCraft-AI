# Evaluation

CareerCraft AI separates **application evaluation** from LLM training. The supplied benchmark in `data/evaluation/` is a small, deterministic sanity benchmark. The recommended research evaluation uses the two Kaggle datasets configured under `data/kaggle/`.

## Recommended evaluation flow

1. Download the Kaggle datasets:

```bash
python scripts/download_kaggle_data.py
```

2. Inspect the downloaded CSV/JSON files. Dataset schemas can change, so the preprocessing step should map their columns into CareerCraft's canonical fields:

```text
resume_text
job_description
resume_category
required_skills
resume_skills
```

3. Run the deterministic benchmark:

```bash
python scripts/run_evaluation.py
```

4. For a final-year report, evaluate at least 50–100 examples and report:

- resume extraction accuracy
- skill extraction precision/recall/F1 where labels are available
- required-skill coverage
- semantic similarity
- alignment-label accuracy on labeled pairs
- unsupported-claim rate
- average latency
- human-rated usefulness/relevance

Do not describe these metrics as hiring prediction accuracy. CareerCraft is a decision-support and document-generation system.
