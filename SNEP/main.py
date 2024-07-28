import requests
import smtplib
from itertools import islice
from secret import API_KEY,NEWS_API_KEY, MY_EMAIL, PASSWORD, TO_EMAIL
from datetime import datetime, timedelta


# Get today's date

today = datetime.today().date()
while (today.weekday() > 4):
    today = today - timedelta(days=1)
print("Today: ", today)
# Calculate yesterday and day before yesterday
yesterday = today - timedelta(days=1)
day_before_yesterday = today - timedelta(days=2)

# Format dates as strings
today_str = today.strftime("%Y-%m-%d")
yesterday_str = yesterday.strftime("%Y-%m-%d")
day_before_yesterday_str = day_before_yesterday.strftime("%Y-%m-%d")

print(today_str)
print(yesterday_str)
print(day_before_yesterday_str)



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

print("yesterday price: ",data["Time Series (Daily)"][yesterday_str]["4. close"])
print("2 days ago price: ",data["Time Series (Daily)"][day_before_yesterday_str]["4. close"])       

print(float(data["Time Series (Daily)"][yesterday_str]["4. close"])-float(data["Time Series (Daily)"][day_before_yesterday_str]["4. close"])  )

first_valid_opening_price = float(data["Time Series (Daily)"][yesterday_str]["4. close"])
second_valid_opening_price = float(data["Time Series (Daily)"][day_before_yesterday_str]["4. close"])

print(first_valid_opening_price)
print(second_valid_opening_price)

percentageIncrease = ((first_valid_opening_price-second_valid_opening_price)/second_valid_opening_price) * 100

if (abs(percentageIncrease) >= 2 ):
    print("Get News, Something happened!!!!")

    def createNews():
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
            #print(newsDict["articles"][0]["source"])
            #print(newsDict["articles"][0]["author"])
            title = newsDict["articles"][0]["title"]
            url = newsDict["articles"][0]["url"]
            #print(newsDict["articles"][0]["publishedAt"])
            return [title,url]
        return []

    def sendEmail(newsData:list):
        if (len(newsData) == 2):
                
            try:
                    
                with smtplib.SMTP("smtp.gmail.com") as connection:
                    connection.starttls()
                    connection.login(user=MY_EMAIL, password=PASSWORD)
                    connection.sendmail(
                        from_addr=MY_EMAIL,
                        to_addrs=TO_EMAIL,
                        msg=f"Subject:{COMPANY_NAME} News\n\nTSLA Stocks Closing Price changed by {round(percentageIncrease,2)}% \nHeadline:{newsData[0]} \nUrl:{newsData[1]}"
                    )
                return("Success")
            except:
                print("Error Encountered")
        return "Terminated"

    sendEmail(createNews())


