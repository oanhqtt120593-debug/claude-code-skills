# SKILL: Weather API

## Mô tả
Skill kết nối OpenWeatherMap API để lấy thông tin thời tiết theo thành phố. Kết quả được lưu vào file output dạng `.txt`.

## Nền tảng kết nối
- **API**: OpenWeatherMap (https://openweathermap.org/api)
- **Loại**: REST API (miễn phí, 60 calls/phút)

## Cách lấy API Key
1. Đăng ký tại https://openweathermap.org/
2. Vào My API Keys → copy key
3. Dán vào biến `API_KEY` trong `weather.py`

## Cách chạy
```bash
python weather.py
```

## Input
- Tên thành phố (nhập trực tiếp khi chạy)

## Output
- In kết quả ra terminal
- Lưu file `output/weather_<city>_<date>.txt`

## Ví dụ output
```
=== THỜI TIẾT: Ho Chi Minh City ===
Ngày      : 2026-05-10 17:00
Trạng thái: Mây rải rác
Nhiệt độ  : 32°C (cảm giác như 36°C)
Độ ẩm     : 75%
Gió       : 3.5 m/s
```

## Files & Folders
```
weather-api/
├── SKILL.md        ← file này
├── weather.py      ← script chính
└── output/         ← kết quả lưu tại đây
```
