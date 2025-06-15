import requests
from datetime import datetime

class WeatherAgent:
    def get_weather_forecast(self, lat, lon, launch_time_utc):
        base_url = "https://api.open-meteo.com/v1/forecast"
        launch_dt = datetime.fromisoformat(launch_time_utc.replace("Z", "+00:00"))
        launch_date = launch_dt.date().isoformat()
        launch_hour = launch_dt.hour

        params = {
            "latitude": lat,
            "longitude": lon,
            "hourly": "temperature_2m,precipitation,wind_speed_10m",
            "start_date": launch_date,
            "end_date": launch_date,
            "timezone": "UTC"
        }

        response = requests.get(base_url, params=params)
        data = response.json()

        index = next((i for i, t in enumerate(data["hourly"]["time"]) if t.startswith(f"{launch_date}T{launch_hour:02d}")), None)

        return {
            "temperature_c": data["hourly"]["temperature_2m"][index] if index is not None else None,
            "precipitation_mm": data["hourly"]["precipitation"][index] if index is not None else 0,
            "wind_speed_kmh": data["hourly"]["wind_speed_10m"][index] if index is not None else None
        }