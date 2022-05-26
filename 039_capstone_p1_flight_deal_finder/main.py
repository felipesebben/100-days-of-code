from data_manager import DataManager
from datetime import datetime as dt, timedelta
from flight_search import FlightSearch
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = 'LON'


# Pass the data from data_manager.py back to main.py
data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_destination_data()
# print(sheet_data)

if sheet_data[0]['iataCode'] == '':
    city_names = [row['city'] for row in sheet_data]
    print(city_names)
    codes = flight_search.get_destination_code(city_names)
    data_manager.update_destination_codes(codes)
    sheet_data = data_manager.get_destination_data()


today = dt.now() + timedelta(1)
six_months_from_today = dt.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination['iataCode'],
        from_time=today,
        to_time=six_months_from_today,
    )

    if flight is not None and flight.price < destination['lowestPrice']:
        notification_manager.send_sms(
            message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} " +
                    f"to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to " +
                    f"{flight.return_date}."
        )
