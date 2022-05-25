import requests
from twilio.rest import Client


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = 'YOUR ALPHAVINTAGE API KEY'
NEWS_API_KEY = 'YOUR NEWS ENDPOINT API KEY'
TWILIO_SID = 'YOUR TWILIO ACCOUNT SID'
TWILIO_AUTH_TOKEN = 'YOUR TWILIO AUTH TOKEN'

# Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries.
stock_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK_NAME,
    'apikey': STOCK_API_KEY,
    }

news_params = {
    'apiKey': NEWS_API_KEY,
    'qInTitle': COMPANY_NAME,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
# print(response.status_code)

data = response.json()['Time Series (Daily)']
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data['4. close'])


# Get the day before yesterday's closing stock price
day_bef_yesterday_closing_price = float(data_list[1]['4. close'])

# Find the positive difference between 1 and 2.
closing_price_diff = yesterday_closing_price - day_bef_yesterday_closing_price
up_down = None
if closing_price_diff > 0:
    up_down = '🔺'
else:
    up_down = '🔻'

# Get the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage_diff = round((closing_price_diff / float(day_bef_yesterday_closing_price)) * 100, 2)
print(percentage_diff)

# If percentage is greater than 5 then print("Get News").
# Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

if abs(percentage_diff) > 5:
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()['articles']

    # Use Python slice operator to create a list that contains the first 3 articles.
    first_3_articles = articles[:3]

    # Create a new list of the first 3 articles headline and description using list comprehension.
    formatted_articles = [f"{STOCK_NAME}: {up_down}{abs(percentage_diff)}% \nHeadline: {article['title']}." +
                          f"\nBrief: {article['description']}" for article in first_3_articles]

    # Send each article as a separate message via Twilio.
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=VIRT_TWILIO_NR,
            to=VERIFIED_NR
            )
