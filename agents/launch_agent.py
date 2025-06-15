import requests

class LaunchAgent:
    def get_next_launch(self):
        url = "https://api.spacexdata.com/v4/launches/next"
        response = requests.get(url)
        data = response.json()

        return {
            "name": data["name"],
            "time": data["date_utc"],
            "site": data["launchpad"]
        }