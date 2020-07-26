#! /usr/bin/env python3
# Fetching Current Weather Data
import json
import sys
import pprint
import requests


def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


print("Program Fetching Current Weather Data")
APP_OPEN_WEATHER_ID = None
with open("open_weather_id") as f:
    APP_OPEN_WEATHER_ID = f.read()

if not APP_OPEN_WEATHER_ID:
    print("Needs a value for APP_OPEN_WEATHER_ID", file=sys.stderr)
if len(sys.argv) < 2:
    print("Usage: 02_get_open_weather.py city_name, 2-letter_country_code", file=sys.stderr)
    sys.exit()

payload = {
    "q": " ".join(sys.argv[1:]),
    "APPID": APP_OPEN_WEATHER_ID
}
r = requests.get("http://api.openweathermap.org/data/2.5/weather", params=payload)

forecast_info = json.loads(r.text)
pprint.pprint(forecast_info)
weather = forecast_info["main"]
temp_max = kelvin_to_celsius(weather["temp_max"])
temp_min = kelvin_to_celsius(weather["temp_min"])
print(f"Current weather: max({temp_max:.2f}C°), min({temp_min:.2f}C°)")
