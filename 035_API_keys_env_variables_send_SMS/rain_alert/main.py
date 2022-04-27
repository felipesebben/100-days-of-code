import requests

OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/onecall?'
api_key = '6ba68fb40b286aaf305469e9e97608b3'

latitude = -30.034647
longitude = -51.217659
parameters = {
    'lat': latitude,
    'lon': longitude,
    'units': 'metric',
    'appid': api_key,
    'exclude': 'current,minutely,daily'
    }

response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()

# Print status code to check whether our request went by.
print(response.status_code)

weather_data = response.json()
hourly_data = list(weather_data.values())
# Get hold of the first 12 hours of the  response by slicing through the json file.
weather_slice = weather_data['hourly'][:12]
# print(weather_data['hourly'][0]['weather'][0]['id'])

will_rain = False

# Loop through the next 12 hours and get hold of the 'id' value of the 'weather' key.
for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Nênee, vai chovê aí, pega um guarda-chuva! 🌂 .")