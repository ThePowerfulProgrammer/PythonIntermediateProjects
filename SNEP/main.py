import requests
import smtplib
from itertools import islice
from secret import API_KEY,NEWS_API_KEY, MY_EMAIL, PASSWORD, TO_EMAIL

# Stock News Email Application

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# parameters = {
#     "function": "TIME_SERIES_DAILY",
#     "symbol": STOCK,
#     "interval":"60min",
#     "outputsize":"compact",
#     "apikey":API_KEY,
    
    
# }
# url = 'https://www.alphavantage.co/query'
# r = requests.get(url, params=parameters)
# data = r.json()

# # print(data["Time Series (Daily)"]["2024-07-25"]["1. open"])
# # print(float(data["Time Series (Daily)"]["2024-07-26"]["1. open"])-float(data["Time Series (Daily)"]["2024-07-25"]["1. open"]))

# # d = {"1": 12, "2": 12}
# # first = dict(islice(d.items(), 1))
# # print(first)

# # yesterdayStockPrice : int 
# # twoDaysAgoStockPrice : int


# first_three = dict(islice(data["Time Series (Daily)"].items(),3))
# yesterdayOpen = first_three["yesterday"]["1. open"]
# dayBeforeYesterdayOpen = first_three["dayBeforeYesterday"]["1. open"]

# percentageIncrease = ((yesterdayOpen-dayBeforeYesterdayOpen)/dayBeforeYesterdayOpen) * 100

# if (abs(percentageIncrease) >= 5 ):
#     print("Get News, Something happened!!!!")




 



## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

newsParameters = {
    "apiKey":NEWS_API_KEY,
    "country":"us",
    "category":"business",
    "q":"Tesla",
}
newsResponse = requests.get("https://newsapi.org/v2/top-headlines",params=newsParameters)

newsResponse.raise_for_status()
newsDict = newsResponse.json()
if (newsDict['totalResults'] > 0):       
    print(newsDict["articles"][0]["source"])
    print(newsDict["articles"][0]["author"])
    title = newsDict["articles"][0]["title"]
    url = newsDict["articles"][0]["url"]
    print(newsDict["articles"][0]["publishedAt"])



## STEP 3: Use SMTP TO email yourself
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
try:
        
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TO_EMAIL,
            msg=f"Subject:{COMPANY_NAME} News\n\nTSLA percentage increase here \nHeadline:{title} \nUrl:{url}"
        )
    print("Success")
except:
    print("Error Encountered")

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

