import requests
from datetime import datetime
import smtplib
import time


MY_LAT = -30.034647
MY_LONG = -51.217659
MY_EMAIL = "fakeseabornlevel@yahoo.com"
MY_PASSWORD = "d#9%SipR7rzy@E+"


def is_iss_overhead():
    """
    Check if the ISS station is passing by our neighborhood.
    """
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_night():
    """
    Check if it is nighttime in our neighborhood.
    """
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_oss_overhead() and is_night():
        connection = smtplib.SMTP('smtp.mail.yahoo.com', port=465)
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject: Look Up 👆\n\nThe ISS is above you in the sky."
        )
