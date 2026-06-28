# python-learning

> A structured Python learning portfolio — from language fundamentals to applied data analytics.

---

## Modules

| Module | Description |
| --- | --- |
| [`01-python-fundamentals/`](01-python-fundamentals/README.md) | Core language concepts through exercises and a CLI project |
| [`02-data-analytics/`](02-data-analytics/README.md) | Applied data analytics from library basics to publication-quality research |

---

## 01 — Python Fundamentals

Eleven focused exercises covering the core Python language, followed by a standalone command-line project.

| Component | Contents |
| --- | --- |
| `exercises/` | Output formatting · variables · types · strings · control flow · validation · data structures |
| `project/dataset-summary/` | CLI tool for CSV structural inspection — standard library only |

→ [`01-python-fundamentals/README.md`](01-python-fundamentals/README.md)

---

## 02 — Data Analytics

Applied analytics using the 2023 Data Jobs dataset throughout, structured as a progression from library fundamentals to a publication-quality multi-notebook study.

| Component | Contents |
| --- | --- |
| `exercises/` | Role matching and type conversion in pure Python |
| `notebooks/` | Pandas and Matplotlib basics, then demand, trend, and compensation analysis for Germany |
| `project/job-market-analysis/` | Five-notebook structured analysis of India's data-job market |

→ [`02-data-analytics/README.md`](02-data-analytics/README.md)

---

## Structure

```text
python-learning/
├── 01-python-fundamentals/
│   ├── exercises/                      # 11 exercises covering core language concepts
│   ├── project/
│   │   └── dataset-summary/            # CSV inspection CLI tool
│   └── README.md
├── 02-data-analytics/
│   └── data-jobs-analysis/
│       ├── exercises/                  # 2 exercises covering data-oriented Python
│       ├── notebooks/                  # 5 analysis notebooks + figures
│       ├── project/
│       │   └── job-market-analysis/    # 5-notebook India market analysis
│       └── README.md
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

---

## Requirements

```bash
pip install -r requirements.txt
```

Module 01 uses the standard library only. Module 02 requires `datasets` · `pandas` · `matplotlib` · `seaborn`.
