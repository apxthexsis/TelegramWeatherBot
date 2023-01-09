import os
import requests
from WeatherInfo import WeatherInfo


class weatherBotClient:

    def __init__(self):
        self.ApiKey = os.getenv("apiKey")
        self.baseurl = "https://api.openweathermap.org/data/2.5/weather"


    def find_weather_for(self, city : str) -> dict:
        params = "?q={city}&appid={api_key}&units=metric"
        call = self.baseurl + params
        url = call.format(city=city, api_key=self.ApiKey)
        resp = requests.get(url)
        return resp.json()

    def retrieve_weather(self, city: str):
        data = self.find_weather_for(city=city)
        weatherDictionary = WeatherInfo.from_dict(data)
        return weatherDictionary
