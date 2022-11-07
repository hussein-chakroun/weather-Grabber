import requests
from pprint import pprint

API_Key = 'b873ac4df99ce6a24a91942f166d7d1c'

city = input("Enter a City: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="

weather_data = requests.get(base_url).json()

pprint(weather_data)