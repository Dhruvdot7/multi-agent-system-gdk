import google.generativeai as genai

class SummaryAgent:
    def __init__(self):
        genai.configure(api_key="Your API key")  # Replace with your real key
        self.model = genai.GenerativeModel("gemini-1.5-flash")  # ← set the model here

    def generate_summary(self, launch_data, weather_data):
        prompt = f"""
        Generate a summary for the following launch:

        Launch Name: {launch_data.get("name")}
        Launch Time: {launch_data.get("net")}
        Launch Site: {launch_data.get("pad", {}).get("id")}

        Weather:
        Temperature: {weather_data.get("temperature_c")}
        Precipitation: {weather_data.get("precipitation_mm")}
        Wind Speed: {weather_data.get("wind_speed_kmh")}
        """

        response = self.model.generate_content(prompt)
        return response.text
