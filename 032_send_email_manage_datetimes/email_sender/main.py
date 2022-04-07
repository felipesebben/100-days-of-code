import smtplib
import datetime as dt
import random


# # Create SMTP object with SMPT() class.
# connection = smtplib.SMTP("smtp.gmail.com", port=587)
#
# # Call start TLS (Transport Layer Security), a way to securing our connection to our email server.
# # This line will encrypt our message and make it secure.
# connection.starttls()
#
# # Log in to account. Use 'with' to avoid having to close the connection later on.
# with connection.login(user=my_email, password=password) as connection:
#     # Send email.
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="fakeseabornlevel@yahoo.com",
#         msg="Subject:Hi!\n\nHere's my mail!"
#     )


# '.now' returnS the current datetime with high accuracy. You can get hold of year, month, weekday...
# year = now.year
# month = now.month
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1987, month=11, day=17, hour=7, minute=37)
# print(date_of_birth)


# Create dummy test email.
MY_EMAIL = ""
MY_PASSWORD= ""

now = dt.datetime.now()
weekday = now.weekday()

with open('quotes.txt', 'r') as f:
    all_quotes = f.readlines()
    random_quote = random.choice(all_quotes)


if weekday == 3:
    with open('quotes.txt', 'r') as f:
        all_quotes = f.readlines()
        random_quote = random.choice(all_quotes)

    print(random_quote)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject: Monday Motivation\n\n{random_quote}"
        )



