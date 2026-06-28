# 01 — Python Fundamentals

> Core language concepts covered through progressive exercises and a CLI project.

---

## Contents

| Path | Description |
| --- | --- |
| `exercises/` | 11 focused exercises covering core Python concepts |
| `project/dataset-summary/` | CLI tool for CSV structural inspection |

---

## Exercises

Each file targets a specific concept or combination of concepts.

| # | File | Concepts |
| --- | --- | --- |
| 01 | `01_print_format_challenge.py` | Multiline strings · escape sequences (`\t`) · tabbed output |
| 02 | `02_variables_contact_output.py` | Variables · f-string formatting |
| 03 | `03_data_types_basic.py` | Built-in types: `int` `float` `str` `bool` `None` · `type()` · `len()` |
| 04 | `04_phone_number_cleaner.py` | String methods · chained `.replace()` |
| 05 | `05_string_clean_summary.py` | String cleaning · `.split()` · character substitution · indexing |
| 06 | `06_random_even_check.py` | `random` module · conditionals · modulo operator |
| 07 | `07_boolean_logic_checks.py` | Boolean expressions · `input()` · validation chains · early exit |
| 08 | `08_email_validation.py` | Guard clauses · TLD checking · multi-rule string validation |
| 09 | `09_password_validation.py` | Compound checks · `.isupper()` · `.islower()` · `.isalnum()` |
| 10 | `10_duplicate_check.py` | Functions · `set()` · duplicate detection |
| 11 | `11_dict_filter_transform.py` | Dict comprehensions · `isinstance()` · type filtering |

---

## Skill Progression

| Stage | Exercises | Focus |
| --- | --- | --- |
| Output & formatting | 01–02 | `print()`, escape sequences, f-strings |
| Types & values | 03 | Built-in types, introspection |
| String manipulation | 04–05 | Cleaning, splitting, substitution |
| Control flow | 06–07 | Conditionals, boolean logic, input handling |
| Validation logic | 08–09 | Guard clauses, multi-rule checks |
| Data structures | 10–11 | Functions, sets, dictionaries, comprehensions |

---

## Project

### dataset-summary

A command-line tool that analyzes CSV files and outputs a human-readable text summary and a structured JSON report. Handles standard and wide/messy formats with no dependencies beyond the standard library.

See [`project/dataset-summary/README.md`](project/dataset-summary/README.md) for full documentation.

```bash
python dataset_summary.py sample_data.csv
```

---

## Structure

```text
01-python-fundamentals/
├── exercises/
│   ├── 01_print_format_challenge.py
│   ├── 02_variables_contact_output.py
│   ├── 03_data_types_basic.py
│   ├── 04_phone_number_cleaner.py
│   ├── 05_string_clean_summary.py
│   ├── 06_random_even_check.py
│   ├── 07_boolean_logic_checks.py
│   ├── 08_email_validation.py
│   ├── 09_password_validation.py
│   ├── 10_duplicate_check.py
│   └── 11_dict_filter_transform.py
└── project/
    └── dataset-summary/
        ├── dataset_summary.py
        ├── sample_data.csv
        ├── summary_report.json
        ├── summary_report.txt
        └── README.md
```

---

## Requirements

- Python 3.x (standard library only)
