from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import requests
from secret import google_form, email, password,site


response = requests.get(url=site)


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

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get(google_form)

# signInBtn = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[1]/div/div[4]/div/div/a[1]')
# sleep(2)
# signInBtn.click()

sleep(2)
# addressLabel = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
# addressLabel.send_keys(addresses[0].text.strip())
# rentLabel = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
# rentLabel.send_keys(cleanedPrices[0])
# linkLabel = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
# linkLabel.send_keys(links[0].get('href'))
# submitBtn = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
# submitBtn.click()

# sleep(2)
# newFormLink.click()

for i in range(44):
    addressLabel = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    rentLabel = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    linkLabel = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submitBtn = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    print("Filling in form ...")
    addressLabel.send_keys(addresses[i].text.strip())
    rentLabel.send_keys(cleanedPrices[i])
    linkLabel.send_keys(links[i].get('href'))
    sleep(1)
    submitBtn.click()
    sleep(1)
    newFormLink = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    newFormLink.click()
    sleep(1)

sleep(3)
driver.quit()

