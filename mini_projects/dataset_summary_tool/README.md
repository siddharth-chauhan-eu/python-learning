# Dataset Summary Tool

Command-line Python tool for analyzing CSV datasets and generating:

- human-readable summary (`.txt`)
- structured report (`.json`)

Designed to handle both:

- standard CSV files
- wide or messy datasets (e.g., World Bank exports)

---

## Capability

Given a CSV file, the tool:

- detects a valid header row (even in messy files)
- extracts usable columns
- computes:
  - total rows and columns
  - missing values (count and percentage)
- infers column types:
  - numeric
  - non-numeric
  - mixed
  - empty

---

## Design Invariant

- no hardcoded column names
- no dataset-specific rules
- parsing is based only on structure

---

## Parsing Approach

The tool uses a two-stage strategy:

1. attempt standard parsing using `csv.DictReader`
2. fallback: scan for a structurally valid header row and retry

This allows handling of irregular or wide datasets.

---

## Type Inference

Columns are classified as:

- `numeric` → all non-empty values are numeric
- `mixed` → combination of numeric and non-numeric values
- `non-numeric` → no numeric values
- `empty` → no non-empty values

---

## Usage

```bash
python dataset_summary.py <csv_file>
```

Example:

```bash
python dataset_summary.py sample_data.csv
```

---

## Output

### Text Report (`summary_report.txt`)

Contains:

- total rows and columns
- column list
- missing values (count and percentage)
- inferred column types

---

### JSON Report (`summary_report.json`)

Structured output:

```json
{
  "file": "sample_data.csv",
  "total_rows": 10,
  "total_columns": 5,
  "columns": ["country", "year", "gdp", "inflation", "notes"],
  "missing": {...},
  "missing_percentage": {...},
  "column_types": {...}
}
```

---

## Assumptions

- delimiter is comma (`,`)
- file fits in memory
- encoding is UTF-8 (BOM supported)

---

## Failure Modes

| Case | Behavior |
|------|----------|
| wrong delimiter (e.g., `;`) | incorrect parsing |
| very large file | high memory usage |
| inconsistent rows | partial parsing issues |
| corrupted CSV | may return empty dataset |

---

## Non-Goals

This tool does not:

- detect delimiters
- validate schemas
- clean or transform data
- perform statistical analysis

---

## Test Coverage

Validated against:

- structured datasets
- edge-case synthetic dataset (`sample_data.csv`)
- real-world messy datasets (e.g., World Bank exports)

Test scenarios include:

- missing values
- invalid numeric values (e.g., `"abc"`)
- mixed-type columns
- malformed rows
- empty fields

---

## Design Principles

- structure over assumptions
- deterministic output
- fail safely (no crashes)
- standard library only

---

## Project Structure

```
dataset_summary_tool/
├── dataset_summary.py
├── sample_data.csv
├── summary_report.txt
├── summary_report.json
└── README.md
```

---

## License

MIT License

---

## Boundary

This tool provides structural inspection, not data validation or cleaning.