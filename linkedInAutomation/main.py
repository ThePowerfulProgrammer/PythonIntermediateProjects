from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from secret import ACCOUNT_EMAIL,ACCOUNT_PASSWORD
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

exampleLink = 'https://www.linkedin.com/jobs/search/?currentJobId=3998076764&distance=25&f_AL=true&f_E=3&geoId=104035573&keywords=developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true'


def makeLinkedInContact(link: str):
    driver = webdriver.Chrome(options=chrome_options)
    
    driver.get(link)
    
    time.sleep(2)
    sign_in_btn = driver.find_element(by=By.LINK_TEXT, value='Sign in')
    sign_in_btn.click()
    
    time.sleep(5)
    email_field = driver.find_element(by=By.ID, value='username')
    email_field.send_keys(ACCOUNT_EMAIL)
    
    password_field = driver.find_element(by=By.ID, value='password')
    password_field.send_keys(ACCOUNT_PASSWORD)
    password_field.send_keys(Keys.ENTER)
    
    input("Press Enter when you have completed")
    
    
makeLinkedInContact(exampleLink)
    