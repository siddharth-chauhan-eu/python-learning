"""
dataset_summary.py

A command-line tool to analyze CSV datasets and generate:
- Human-readable text summary
- Structured JSON report

Handles standard CSVs and wide-format datasets (e.g., World Bank exports).
"""

import csv
import sys
import json
from pathlib import Path


def read_csv_file(file_path):
    """
    Read and parse a CSV file into a list of dictionaries.

    Strategy:
    1. Attempt standard CSV parsing.
    2. Fallback: detect correct header row for wide/messy datasets.

    Args:
        file_path (Path): Path to the CSV file.

    Returns:
        list[dict]: Parsed rows, or empty list if parsing fails.
    """
    with open(file_path, mode="r", encoding="utf-8-sig") as file:
        lines = file.readlines()

    # Step 1: Standard CSV parsing
    try:
        reader = csv.DictReader(lines)
        rows = list(reader)

        if rows:
            columns = [c for c in rows[0].keys() if c and c.strip()]
            if len(columns) >= 3:
                return rows
    except Exception:
        pass  # Fallback handles failure

    # Step 2: Fallback for wide datasets
    for i, line in enumerate(lines):
        if line.count(",") >= 10:
            try:
                reader = csv.DictReader(lines[i:])
                rows = list(reader)

                if rows:
                    columns = [c for c in rows[0].keys() if c and c.strip()]
                    if len(columns) >= 3:
                        return rows
            except Exception:
                continue

    return []


def count_missing_values(rows, columns):
    """
    Count missing (empty or null) values per column.
    """
    missing = {}

    for col in columns:
        missing[col] = sum(
            1
            for row in rows
            if row.get(col) is None or (row.get(col) or "").strip() == ""
        )

    return missing


def is_number(value):
    """
    Check if a value can be converted to a float.
    """
    try:
        float(value)
        return True
    except ValueError:
        return False


def analyze_column_types(rows, columns):
    """
    Infer data type of each column.
    """
    types = {}

    for col in columns:
        values = [(row.get(col) or "").strip() for row in rows]
        non_empty = [v for v in values if v]

        numeric_count = sum(1 for v in non_empty if is_number(v))
        total = len(non_empty)

        if total == 0:
            types[col] = "empty"
        elif numeric_count == total:
            types[col] = "numeric"
        elif numeric_count > 0:
            types[col] = "mixed"
        else:
            types[col] = "non-numeric"

    return types


def generate_summary(rows, file_name):
    """
    Generate dataset summary (text + structured metrics).
    """
    if not rows:
        return "Empty dataset", {}, {}, {}, []

    columns = [col for col in rows[0].keys() if col and col.strip()]

    summary = [
        "=" * 30,
        "Dataset Summary Report",
        f"File: {file_name}",
        "",
        f"Total Rows: {len(rows)}",
        f"Total Columns: {len(columns)}",
        "",
        "Columns:",
        *[f"- {col}" for col in columns],
        "",
        "Missing Values:",
    ]

    missing = count_missing_values(rows, columns)
    summary.extend(f"- {col}: {count}" for col, count in missing.items())

    summary.append("\nMissing Percentage:")
    missing_percentage = {}

    for col, count in missing.items():
        percent = (count / len(rows)) * 100
        missing_percentage[col] = round(percent, 2)
        summary.append(f"- {col}: {percent:.2f}%")

    summary.append("\nColumn Types (inferred):")

    column_types = analyze_column_types(rows, columns)
    summary.extend(f"- {col}: {ctype}" for col, ctype in column_types.items())

    summary.append("=" * 30)

    return "\n".join(summary), missing, missing_percentage, column_types, columns


def save_report(text, output_path):
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(text)


def save_json_report(data, output_path):
    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, sort_keys=True)


def main():
    """
    CLI entry point.
    """
    if len(sys.argv) < 2:
        print("Usage: python dataset_summary.py <csv_file>")
        return

    input_file = Path(sys.argv[1])
    base_path = Path(__file__).parent

    txt_output = base_path / "summary_report.txt"
    json_output = base_path / "summary_report.json"

    if not input_file.exists():
        print("CSV file not found.")
        return

    rows = read_csv_file(input_file)

    # Failure handling
    if not rows:
        print("Parsing failed: unsupported structure or delimiter")
        return

    summary_text, missing, missing_percentage, column_types, columns = generate_summary(
        rows, input_file.name
    )

    save_report(summary_text, txt_output)

    json_data = {
        "file": input_file.name,
        "total_rows": len(rows),
        "total_columns": len(columns),
        "columns": columns,
        "missing": missing,
        "missing_percentage": missing_percentage,
        "column_types": column_types,
    }

    save_json_report(json_data, json_output)

    print("Summary generated successfully.")
    print(f"Processed file: {input_file.name}")
    print("Generated files: summary_report.txt, summary_report.json")


if __name__ == "__main__":
    main()
