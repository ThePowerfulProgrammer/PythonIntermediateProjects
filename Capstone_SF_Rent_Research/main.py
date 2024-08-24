from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
import re


response = requests.get(url='https://appbrewery.github.io/Zillow-Clone/')


soup = BeautifulSoup(response.text, 'html.parser')


# Found all addresses
addresses = soup.find_all(name='address')
for add in addresses:
    print(add.text.strip())

# Found all prices
prices = soup.find_all(name='span', attrs={'data-test':"property-card-price"})
cleanedPrices = [price.text[0:6] for price in prices]
for price in cleanedPrices:
    print(price)
    
# Found all links
links = soup.find_all('a',class_='property-card-link')

for link in links:
    print(link.get('href'))
    
    
# I have all my data --> 44 forms that I need to fill.

