import csv
import sys
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
    for col, count in missing.items():
        percent = (count / len(rows)) * 100
        summary.append(f"- {col}: {percent:.2f}%")

    summary.append("")
    summary.append("Column Types (inferred):")

    for col in columns:
        values = [
            (row.get(col) or "").strip()
            for row in rows
        ]

        non_empty_values = [v for v in values if v != ""]

        numeric_count = sum(
            1 for v in non_empty_values if is_number(v)
        )
        total_non_empty = len(non_empty_values)

        if total_non_empty == 0:
            summary.append(f"- {col}: empty")
        elif numeric_count == total_non_empty:
            summary.append(f"- {col}: numeric")
        elif numeric_count > 0:
            summary.append(f"- {col}: mixed")
        else:
            summary.append(f"- {col}: non-numeric")

    summary.append("=" * 30)

    return "\n".join(summary)


def save_report(text, output_path):
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(text)


def main():
    if len(sys.argv) < 2:
        print("Usage: python dataset_summary.py <csv_file>")
        return

    input_file = Path(sys.argv[1])
    output_file = Path(__file__).parent / "summary_report.txt"

    if not input_file.exists():
        print("CSV file not found.")
        return

    rows = read_csv_file(input_file)
    summary = generate_summary(rows, input_file.name)
    save_report(summary, output_file)

    print("Summary generated successfully.")
    print(f"Processed file: {input_file.name}")


if __name__ == "__main__":
    main()