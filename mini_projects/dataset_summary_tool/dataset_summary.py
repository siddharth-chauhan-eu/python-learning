import csv
import sys
import json
from pathlib import Path


def read_csv_file(file_path):
    with open(file_path, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


def count_missing_values(rows, columns):
    missing = {}

    for col in columns:
        missing[col] = 0
        for row in rows:
            value = row.get(col, "")
            if value is None or value.strip() == "":
                missing[col] += 1

    return missing


def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def analyze_column_types(rows, columns):
    types = {}

    for col in columns:
        values = [(row.get(col) or "").strip() for row in rows]
        non_empty_values = [v for v in values if v != ""]

        numeric_count = sum(1 for v in non_empty_values if is_number(v))
        total_non_empty = len(non_empty_values)

        if total_non_empty == 0:
            types[col] = "empty"
        elif numeric_count == total_non_empty:
            types[col] = "numeric"
        elif numeric_count > 0:
            types[col] = "mixed"
        else:
            types[col] = "non-numeric"

    return types


def generate_summary(rows, file_name):
    if not rows:
        return "Empty dataset"

    columns = list(rows[0].keys())

    summary = []
    summary.append("=" * 30)
    summary.append("Dataset Summary Report")
    summary.append(f"File: {file_name}")
    summary.append("")

    summary.append(f"Total Rows: {len(rows)}")
    summary.append(f"Total Columns: {len(columns)}")
    summary.append("")

    summary.append("Columns:")
    for col in columns:
        summary.append(f"- {col}")

    summary.append("")
    summary.append("Missing Values:")

    missing = count_missing_values(rows, columns)
    for col, count in missing.items():
        summary.append(f"- {col}: {count}")

    summary.append("")
    summary.append("Missing Percentage:")
    missing_percentage = {}
    for col, count in missing.items():
        percent = (count / len(rows)) * 100
        missing_percentage[col] = round(percent, 2)
        summary.append(f"- {col}: {percent:.2f}%")

    summary.append("")
    summary.append("Column Types (inferred):")

    column_types = analyze_column_types(rows, columns)
    for col, col_type in column_types.items():
        summary.append(f"- {col}: {col_type}")

    summary.append("=" * 30)

    return "\n".join(summary), missing, missing_percentage, column_types, columns


def save_report(text, output_path):
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(text)


def save_json_report(data, output_path):
    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def main():
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
