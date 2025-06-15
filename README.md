# 🚀 Multi-Agent AI System

## 🔍 Overview
A modular multi-agent AI system that:
- Fetches upcoming SpaceX launch data
- Retrieves weather forecast for the launch site
- Uses Google Gemini (GDK) to summarize the mission and conditions

## 📦 Agents
- **Launch Agent**: Gets next launch details using SpaceX API
- **Weather Agent**: Gets weather forecast via Open-Meteo API
- **Summary Agent**: Uses Gemini to summarize and analyze

## 🛠 Setup

### 1. Clone & Install
```bash
git clone https://github.com/yourname/multi-agent-ai-system.git
cd multi-agent-ai-system
pip install -r requirements.txt
```

### 2. Add `.env`
Create a `.env` file with:
```
GEMINI_API_KEY=your_api_key_here
```

### 3. Run
```bash
python main.py
```

## 📌 Dependencies
- Python 3.8+
- Google Generative AI SDK
- Requests, dotenv

## ✅ Output
A real-time report of the next launch, weather, and smart summary.

## ⚠️ Known Limitation: Weather Data and Summary Generation

The system relies on accurate weather data (`temperature_c`, `wind_speed_kmh`, `precipitation_mm`) to generate a rich launch summary.

### What Happens If Data Is Missing?
If these values are missing or set to `None`, the AI model will generate a fallback summary stating that information is unavailable.

### How to Fix It
- Integrate a real weather API (e.g., OpenWeatherMap or WeatherAPI).
- Or, for testing/demo purposes, manually hardcode mock data:

```python
weather = {
  'temperature_c': 27,
  'precipitation_mm': 0,
  'wind_speed_kmh': 15
}
