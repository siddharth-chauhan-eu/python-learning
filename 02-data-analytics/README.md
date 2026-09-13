# 02 — Data Analytics

> From DataFrame basics to evidence-aware analysis using real-world job-posting data.

This module builds applied data analytics capability in a single coherent arc — exercises establish Python patterns for structured data, notebooks develop library skills and apply them to Germany's data-job market, and a project extends the methodology into a structured five-notebook study of India.

---

## Contents

| Path | Description |
| --- | --- |
| `data-jobs-analysis/` | Exercises, notebooks, and project using the 2023 Data Jobs dataset |

---

## Learning Arc

| Phase | Location | Focus |
| --- | --- | --- |
| Foundations | `exercises/` | Role matching · type conversion · data cleaning in pure Python |
| Library basics | `notebooks/01–02` | Pandas operations and first Matplotlib visualisation |
| Analysis | `notebooks/03–05` | Demand, trends, and compensation for Germany's data-job market |
| Project | `project/job-market-analysis/` | Five-notebook structured study of India's data-job market |

---

## Dataset

The notebooks and project use the [Luke Barousse Data Jobs dataset](https://huggingface.co/datasets/lukebarousse/data_jobs) — a collection of data-role job postings from calendar year 2023, covering multiple countries and role types. The pure-Python exercises use small in-repository examples rather than the external dataset.

---

## Requirements

```bash
pip install -r requirements.txt
```

Dependencies: `datasets` · `pandas` · `matplotlib` · `numpy` · `seaborn`

---

See [`data-jobs-analysis/README.md`](data-jobs-analysis/README.md) for full documentation.
