from agents.launch_agent import LaunchAgent
from agents.weather_agent import WeatherAgent
from agents.summary_agent import SummaryAgent

def main():
    print("🚀 Starting Multi-Agent AI System...\n")

    launch_agent = LaunchAgent()
    weather_agent = WeatherAgent()
    summary_agent = SummaryAgent()

    launch = launch_agent.get_next_launch()
    print(f"🛰 Launch Name: {launch['name']}")
    print(f"   Launch Time: {launch['time']}")
    print(f"   Launch Site: {launch['site']}\n")

    lat, lon = 28.6084, -80.6043
    weather = weather_agent.get_weather_forecast(lat, lon, launch["time"])

    print("🌦 Weather Forecast:")
    print(weather)

    print("\n📄 Generating summary...")
    summary = summary_agent.generate_summary(launch, weather)
    print("\n📝 Summary:\n", summary)

if __name__ == "__main__":
    main()
# NOTE:
# The generated summary may be incomplete or generic if weather data is missing or null.
# To ensure a rich summary output, verify that the weather_agent returns actual values
# for temperature_c, wind_speed_kmh, and precipitation_mm.
#
# Example Fix:
# - Use a real weather API (e.g., OpenWeatherMap) OR
# - Provide fallback dummy values during testing.
#
# Example:
# weather = {
#     'temperature_c': 27,
#     'precipitation_mm': 0,
#     'wind_speed_kmh': 15
# }
#
# Without this, the summary_agent may return a placeholder message indicating missing data.
