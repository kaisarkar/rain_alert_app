import requests

MY_API_KEY = "423b47d5b3cd4d3f646f94d07ba0570c"
ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
params = {
    "lat": 22.899701,
    "lon": 88.394763,
    "cnt": 4,
    "appid": MY_API_KEY,
}

with requests.get(ENDPOINT, params=params) as response:
    response.raise_for_status()
    data = response.json()
    print(data)