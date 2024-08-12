from bs4 import BeautifulSoup
import requests
from .secret import CLIENT_ID,CLIENT_SECRET

date = input("Which uear do you want to travel to? Type the date in this format YYYY-MM-DD: ").upper()


response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{date}/")

soup = BeautifulSoup(markup=response.text)

print(soup.prettify())

