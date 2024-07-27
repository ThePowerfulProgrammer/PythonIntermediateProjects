import requests
import smtplib
from itertools import islice
from secret import API_KEY

# Stock News Email Application

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "interval":"60min",
    "outputsize":"compact",
    "apikey":API_KEY,
    
    
}
url = 'https://www.alphavantage.co/query'
r = requests.get(url, params=parameters)
data = r.json()



print(data)
# print(data["Time Series (Daily)"]["2024-07-25"]["1. open"])
# print(float(data["Time Series (Daily)"]["2024-07-26"]["1. open"])-float(data["Time Series (Daily)"]["2024-07-25"]["1. open"]))

# d = {"1": 12, "2": 12}
# first = dict(islice(d.items(), 1))
# print(first)

# yesterdayStockPrice : int 
# twoDaysAgoStockPrice : int

 



## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
