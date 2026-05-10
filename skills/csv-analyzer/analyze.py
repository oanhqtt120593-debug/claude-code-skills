import csv
import os
import sys
from datetime import datetime


def read_csv(filepath):
    rows = []
    with open(filepath, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames
        for row in reader:
            rows.append(row)
    return headers, rows


def is_numeric(values):
    try:
        [float(v.replace(",", "")) for v in values if v.strip()]
        return True
    except ValueError:
        return False


def stats(values):
    nums = [float(v.replace(",", "")) for v in values if v.strip()]
    if not nums:
        return None
    return {
        "total": sum(nums),
        "avg": sum(nums) / len(nums),
        "min": min(nums),
        "max": max(nums),
    }


def format_number(n):
    return f"{n:,.0f}"


def analyze(headers, rows):
    numeric_cols = {}
    text_cols = {}

    for col in headers:
        values = [row[col] for row in rows]
        if is_numeric(values):
            numeric_cols[col] = stats(values)
        else:
            unique = list(set(values))
            text_cols[col] = {"unique_count": len(unique), "values": unique[:5]}

    return numeric_cols, text_cols


def build_numeric_table(numeric_cols):
    if not numeric_cols:
        return "_Không có cột số_"
    lines = ["| Cột | Tổng | Trung bình | Min | Max |", "|-----|------|-----------|-----|-----|"]
    for col, s in numeric_cols.items():
        lines.append(
            f"| {col} | {format_number(s['total'])} | {format_number(s['avg'])} | {format_number(s['min'])} | {format_number(s['max'])} |"
        )
    return "\n".join(lines)


def build_text_table(text_cols):
    if not text_cols:
        return "_Không có cột văn bản_"
    lines = ["| Cột | Số giá trị duy nhất | Mẫu giá trị |", "|-----|---------------------|-------------|"]
    for col, info in text_cols.items():
        sample = ", ".join(info["values"])
        lines.append(f"| {col} | {info['unique_count']} | {sample} |")
    return "\n".join(lines)


def build_report(filename, headers, rows, numeric_cols, text_cols):
    template_path = os.path.join(os.path.dirname(__file__), "templates", "report_template.md")
    with open(template_path, encoding="utf-8") as f:
        template = f.read()

    return template.format(
        filename=filename,
        date=datetime.now().strftime("%Y-%m-%d %H:%M"),
        row_count=len(rows),
        col_count=len(headers),
        columns=", ".join(headers),
        numeric_table=build_numeric_table(numeric_cols),
        text_table=build_text_table(text_cols),
    )


def save_report(report, filename):
    os.makedirs("output", exist_ok=True)
    base = os.path.splitext(os.path.basename(filename))[0]
    date_str = datetime.now().strftime("%Y%m%d_%H%M")
    out_path = f"output/report_{base}_{date_str}.md"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(report)
    return out_path


def print_summary(filename, rows, headers, numeric_cols):
    print(f"\n=== PHAN TICH: {filename} ===")
    print(f"  So dong  : {len(rows)}")
    print(f"  So cot   : {len(headers)}")
    if numeric_cols:
        print("\n  Thong ke nhanh:")
        for col, s in numeric_cols.items():
            print(f"    {col}: tong={format_number(s['total'])}, tb={format_number(s['avg'])}")


def main():
    if len(sys.argv) < 2:
        default = os.path.join(os.path.dirname(__file__), "data", "sample_sales.csv")
        filepath = input(f"Nhap duong dan file CSV [{default}]: ").strip() or default
    else:
        filepath = sys.argv[1]

    if not os.path.exists(filepath):
        print(f"Loi: Khong tim thay file '{filepath}'")
        sys.exit(1)

    print(f"Dang phan tich: {filepath}")
    headers, rows = read_csv(filepath)
    numeric_cols, text_cols = analyze(headers, rows)

    print_summary(os.path.basename(filepath), rows, headers, numeric_cols)

    report = build_report(os.path.basename(filepath), headers, rows, numeric_cols, text_cols)
    out_path = save_report(report, filepath)
    print(f"\nDa luu bao cao: {out_path}")


if __name__ == "__main__":
    main()
