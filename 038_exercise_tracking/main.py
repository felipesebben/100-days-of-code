import requests
from datetime import datetime as dt
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='file.env')

GENDER = 'male'
AGE = 34
HEIGHT = 179
WEIGHT = 87.5

APP_ID = os.getenv("NT_APP_ID")
API_KEY = os.getenv('NT_API_KEY')

nutrionix_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
sheety_endpoint = os.getenv('SHEETY_ENDPOINT')

exercise_query = input("Tell me which exercises you did: ")

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
    'Content-Type': 'application/json'
}

user_params ={
    "query": exercise_query,
    'gender': GENDER,
    'weight_kg': WEIGHT,
    'height_cm': HEIGHT,
    'age': AGE
}

response = requests.post(nutrionix_endpoint, json=user_params, headers=headers)
data = response.json()
print(data)

today_time = dt.now().strftime('%d/%m/%Y')
now_time = dt.now().strftime('%X')

for exercise in data['exercises']:
    sheety_params = {
        'workout': {
            'date': today_time,
            'time': now_time,
            'exercise': exercise['name'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories'],
        }
    }

    bearer_headers = {
        'authorization': f"Bearer {os.getenv('TOKEN')}"
    }
    sheety_response = requests.post(
        sheety_endpoint,
        json=sheety_params,
        headers=bearer_headers
    )

    print(sheety_response.text)





