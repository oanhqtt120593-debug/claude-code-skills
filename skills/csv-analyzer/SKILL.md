# SKILL: CSV Analyzer

## Mô tả
Skill đọc file CSV, tính toán thống kê cơ bản (tổng, trung bình, min, max) và xuất báo cáo ra file Markdown.

## Cách chạy
```bash
python analyze.py data/sample_sales.csv
```
Hoặc nhập tên file CSV tùy ý:
```bash
python analyze.py <đường_dẫn_file.csv>
```

## Input
- File `.csv` đặt trong thư mục `data/`

## Output
- Báo cáo phân tích lưu tại `output/report_<tên_file>_<ngày>.md`
- In tóm tắt ra terminal

## Files & Folders
```
csv-analyzer/
├── SKILL.md              ← file này
├── analyze.py            ← script phân tích chính
├── data/
│   └── sample_sales.csv  ← file CSV mẫu
├── output/               ← báo cáo xuất ra đây
└── templates/
    └── report_template.md ← mẫu báo cáo
```

## Ví dụ output
```markdown
# Báo cáo phân tích: sample_sales.csv
**Ngày tạo:** 2026-05-10

## Tổng quan
- Số dòng dữ liệu: 10
- Số cột: 4

## Thống kê cột số
| Cột | Tổng | Trung bình | Min | Max |
|-----|------|-----------|-----|-----|
| Revenue | 150,000 | 15,000 | 5,000 | 30,000 |
```
