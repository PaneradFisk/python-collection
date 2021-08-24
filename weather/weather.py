# Check weather in a city using OpenWeatherMap API
# api.openweathermap.org/data/2.5/weather?q={city}&lang=sv&appid={API_KEY}&units=metric

# Script written with/for Swedish output

import requests
from requests.models import Response
from requests.sessions import requote_uri
import json
import os
from dotenv import load_dotenv

load_dotenv()


api_key = os.environ.get("APIKEY")
URL = "http://api.openweathermap.org/data/2.5/weather?"
city = input("Välj stad: ")


# Setup parameters for complete URL
parameters = {"lang": "sv", "units": "metric", "appid": api_key, "q": city}

response = requests.get(url=URL, params=parameters)
response.raise_for_status()


# Load JSON data into a Python variable
weatherData = json.loads(response.text)


# Compute Python variables from response
w_main = weatherData["main"]
w_desc = weatherData["weather"]
temp = str(w_main["temp"])
feels_like = str(w_main["feels_like"])
looks_like = str(w_desc[0]["description"]).capitalize()


# Print weather descriptions.
print("-" * 30)
print("Vädret i", city.capitalize() + ":")
print("Temperatur:", temp + "c")
print("Känns som:", feels_like + "c")
print("Väder just nu:", looks_like)
print("-" * 30)
