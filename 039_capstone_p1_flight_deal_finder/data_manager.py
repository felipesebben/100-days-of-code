import os
import requests
from dotenv import load_dotenv
from pprint import pprint

load_dotenv(dotenv_path='file.env')

SHEETY_ENDPOINT = os.getenv('SHEETY_ENDPOINT')


class DataManager:
    """This class is responsible for talking to the Google Sheet."""

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        """Use the Sheety API to get all the data in the sheet and print it out."""
        response = requests.get(url=SHEETY_ENDPOINT)
        data = response.json()
        self.destination_data = data['prices']
        # Use pprint to print the data properly formatted.
        # print(pprint(data))
        return self.destination_data

    # Make Put request and use row from sheet_data to update Google Sheet with the IATA codes.
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                'price': {
                    'iataCode': city['iataCode']
                }
            }
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
