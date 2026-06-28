# 02 — Data Analytics

> From DataFrame basics to publication-quality research, using real-world job market data throughout.

This module builds applied data analytics capability in a single coherent arc — exercises establish the Python patterns needed to handle structured data, notebooks develop library skills and apply them to Germany's data-job market, and a project delivers the same analysis at publication quality for the Indian market.

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

All work in this module uses the [Luke Barousse Data Jobs dataset](https://huggingface.co/datasets/lukebarousse/data_jobs) — a collection of data-role job postings from calendar year 2023, covering multiple countries and role types.

---

## Requirements

```bash
pip install -r requirements.txt
```

Dependencies: `datasets` · `pandas` · `matplotlib` · `seaborn`

---

See [`data-jobs-analysis/README.md`](data-jobs-analysis/README.md) for full documentation.
