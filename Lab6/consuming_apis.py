import os
import requests
from datetime import datetime

# Minneapolis
lat = 44.97
lon = -93.26
# Always request metric and convert to Fahrenheit ourselves for clarity/consistency
units = 'metric'  # API request units

api_key = os.environ.get('WEATHER_KEY')  # Set this environment variable on your computer

def to_fahrenheit(celsius: float) -> float:
    return celsius * 9 / 5 + 32

def format_ts(unix_ts: int) -> str:
    try:
        # OpenWeather 'dt' is UTC. Show human-readable UTC time.
        return datetime.utcfromtimestamp(unix_ts).strftime('%Y-%m-%d %H:%M UTC')
    except Exception:
        return str(unix_ts)

def fetch_forecast(lat: float, lon: float, units: str, api_key: str):
    if not api_key:
        raise RuntimeError("WEATHER_KEY environment variable is not set.")
    url = (
        f'https://api.openweathermap.org/data/2.5/forecast'
        f'?lat={lat}&lon={lon}&units={units}&appid={api_key}'
    )
    try:
        resp = requests.get(url, timeout=15)
        resp.raise_for_status()
        data = resp.json()
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Network or HTTP error while calling weather API: {e}") from e
    except ValueError as e:
        raise RuntimeError(f"Failed to parse JSON from weather API: {e}") from e

    # OpenWeather returns 'cod' as string, e.g., "200"
    cod = data.get('cod')
    if cod != "200":
        message = data.get('message', 'Unknown error')
        raise RuntimeError(f"Weather API returned error code {cod}: {message}")

    if 'list' not in data or not isinstance(data['list'], list):
        raise RuntimeError("Unexpected API response: missing 'list' field.")

    return data

def print_forecast(data: dict):
    city = data.get('city', {}).get('name', 'Unknown City')
    country = data.get('city', {}).get('country', '')
    header = f"5-Day Forecast for {city}, {country}".strip().strip(',')
    print(header)
    print('-' * len(header))

    entries = data['list']  # 3-hour intervals
    if not entries:
        print("No forecast data available.")
        return

    for item in entries:
        dt_val = item.get('dt')
        main = item.get('main', {})
        wind = item.get('wind', {})
        weather_arr = item.get('weather', [])

        temp_c = main.get('temp')
        temp_f = to_fahrenheit(temp_c) if isinstance(temp_c, (int, float)) else None
        desc = (weather_arr[0].get('description') if weather_arr else 'N/A') or 'N/A'
        wind_speed_ms = wind.get('speed')  # meters/sec when units=metric

        ts = format_ts(dt_val if isinstance(dt_val, int) else 0)

        temp_part = f"{temp_f:.1f} F" if temp_f is not None else "N/A"
        wind_part = f"{wind_speed_ms:.1f} m/s" if isinstance(wind_speed_ms, (int, float)) else "N/A"

        print(f"{ts} | Temp: {temp_part} | Weather: {desc} | Wind: {wind_part}")

def main():
    try:
        data = fetch_forecast(lat=lat, lon=lon, units=units, api_key=api_key)
        print_forecast(data)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()