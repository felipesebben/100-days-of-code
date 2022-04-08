import requests
from datetime import datetime
MY_LAT = -30.034647
MY_LONG = -51.217659

# Call .get() to retrieve data from endpoint. Store it as response.
# response = requests.get(url='http://api.open-notify.org/iss-now.json')
# print(response.status_code)  # Use status_code to get the response status code.

# Some response codes:
# 1XX - hold on
# 2XX - here you go
# 3XX - what are you doing here
# 4XX - you screwed up
# 5XX - the server screwed up

# Dealing with errors. Requests has a raise_for_status() just for that!
# response.raise_for_status()
#
# data = response.json()
#
# long = data['iss_position']['longitude']
# lat = data['iss_position']['latitude']
#
# iss_position = (long, lat)
# print(iss_position)


parameters = {
    'lat': MY_LAT,
    'lng': MY_LONG,
    'formatted': 0,
}

#  Sunset and Sunrise API used with ISS API to spot the satellite.
response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data['results']['sunrise'].split('T')[1].split(':')[0]
sunset = data['results']['sunset'].split('T')[1].split(':')[0]
print(sunrise)
print(sunset)

time_now = datetime.now()

# print(time_now)