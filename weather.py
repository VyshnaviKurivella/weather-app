import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    
    if response.status_code == 200:
        print(f"\nWeather in {city}:")
        print(f"  Condition  : {data['weather'][0]['description']}")
        print(f"  Temperature: {data['main']['temp']}°C")
        print(f"  Feels like : {data['main']['feels_like']}°C")
        print(f"  Humidity   : {data['main']['humidity']}%")
    else:
        print(f"Error: {data['message']}")

city = input("Enter city name: ")
get_weather(city)