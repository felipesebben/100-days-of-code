import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='file.env')

TOKEN = os.getenv('TOKEN')
USER_NAME = os.getenv('USER_NAME')

# USERNAME = 'sebbenf'
GRAPH_ID = 'graph1'

# Create user account
pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'token': TOKEN,
    'username': USER_NAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
    }

# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)

# Create a graph definition.

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config = {
    'id': 'graph1',
    'name': 'Exercise Graph',
    'unit': 'min',
    'type': 'int',
    'color': 'sora',
    }

headers = {
    'X-USER-TOKEN': TOKEN
}
# response = requests.post(graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Post a pixel.

post_pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"

today = datetime.now()
# print(today.strftime('%Y%m%d'))

post_pixel_config = {
    'date': today.strftime('%Y%m%d'),
    'quantity': input("How many minutes did you exercise today? "),
}

# response = requests.post(post_pixel_endpoint, json=post_pixel_config, headers=headers)
# print(response.text)

# Update posts.

update_posts_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

update_posts_config = {
    'quantity': '67',
}

# response = requests.put(url=update_posts_endpoint, json=update_posts_config, headers=headers)
# print(response.text)

# Delete posts.

yesterday = datetime(year=2022, month=5, day=8)

delete_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{yesterday.strftime('%Y%m%d')}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
