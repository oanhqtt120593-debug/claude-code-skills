import sys
import io
import urllib.request
import urllib.parse
import json
from datetime import datetime
import os

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

API_KEY = "22ca636c209dd0f1bfd1cf9f00ce0b7b"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

WEATHER_VI = {
    "Clear": "Troi nang",
    "Clouds": "Co may",
    "Rain": "Mua",
    "Drizzle": "Mua phun",
    "Thunderstorm": "Giong bao",
    "Snow": "Tuyet",
    "Mist": "Suong mu",
    "Fog": "Suong day",
    "Haze": "Mo suong",
}


def kelvin_to_celsius(k):
    return round(k - 273.15, 1)


def get_weather(city):
    url = f"{BASE_URL}?q={urllib.parse.quote(city.strip())}&appid={API_KEY}"
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
    except urllib.error.HTTPError as e:
        if e.code == 401:
            print("Loi: API Key chua duoc kich hoat hoac khong hop le.")
            print("Key moi can cho 10-30 phut. Thu lai sau!")
        elif e.code == 404:
            print(f"Loi: Khong tim thay thanh pho '{city}'")
        else:
            print(f"Loi HTTP: {e.code}")
        return None

    main = data["main"]
    weather_code = data["weather"][0]["main"]
    weather_desc = WEATHER_VI.get(weather_code, data["weather"][0]["description"])

    return {
        "city": data["name"],
        "country": data["sys"]["country"],
        "datetime": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "status": weather_desc,
        "temp": kelvin_to_celsius(main["temp"]),
        "feels_like": kelvin_to_celsius(main["feels_like"]),
        "humidity": main["humidity"],
        "wind_speed": data["wind"]["speed"],
    }


def format_report(w):
    return (
        f"=== THOI TIET: {w['city']}, {w['country']} ===\n"
        f"Ngay      : {w['datetime']}\n"
        f"Trang thai: {w['status']}\n"
        f"Nhiet do  : {w['temp']}C (cam giac nhu {w['feels_like']}C)\n"
        f"Do am     : {w['humidity']}%\n"
        f"Gio       : {w['wind_speed']} m/s"
    )


def save_output(city, report):
    os.makedirs("output", exist_ok=True)
    date_str = datetime.now().strftime("%Y%m%d_%H%M")
    filename = f"output/weather_{city.strip().replace(' ', '_')}_{date_str}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"\nDa luu ket qua vao: {filename}")


def main():
    city = input("Nhap ten thanh pho (VD: Hanoi, Ho Chi Minh City): ").strip().lstrip("﻿")
    if not city:
        city = "Hanoi"

    print(f"\nDang lay du lieu thoi tiet cho '{city}'...")
    weather = get_weather(city)

    if weather:
        report = format_report(weather)
        print("\n" + report)
        save_output(city, report)


if __name__ == "__main__":
    main()
