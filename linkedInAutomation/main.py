from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from secret import ACCOUNT_EMAIL,ACCOUNT_PASSWORD, name,surname, address, number
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

exampleLink = 'https://www.linkedin.com/jobs/search/?currentJobId=3994565912&distance=25&f_AL=true&f_E=3&geoId=104035573&keywords=developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true'


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
    
    
    time.sleep(20)
    # Grab easy apply button and click it
    easyApplybtn = driver.find_element(By.XPATH, value="/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[6]/div/div/div/button")
    easyApplybtn.click()
    
    time.sleep(2)
    firstNameInput = driver.find_element(By.XPATH, value='/html/body/div[3]/div/div/div[2]/div/div[2]/form/div/div[1]/div[2]/div/div/div[1]/div/input')
    firstNameInput.clear()
    firstNameInput.send_keys(name)
    
    lastNameInput = driver.find_element(By.XPATH, value='/html/body/div[3]/div/div/div[2]/div/div[2]/form/div/div[1]/div[3]/div/div/div[1]/div/input')
    lastNameInput.clear()
    lastNameInput.send_keys(surname)
    
    
    phoneCountryCode = driver.find_element(By.XPATH, value='/html/body/div[3]/div/div/div[2]/div/div[2]/form/div/div[1]/div[4]/div/div/select')
    phoneCountryCode.clear()
    phoneCountryCode.send_keys("South Africa")
    
    
    phoneNumber = driver.find_element(By.XPATH, value='/html/body/div[3]/div/div/div[2]/div/div[2]/form/div/div[1]/div[5]/div/div/div[1]/div/input')
    phoneCountryCode.clear()
    phoneNumber.send_keys(number)
    
    address = driver.find_element(By.XPATH, value='/html/body/div[3]/div/div/div[2]/div/div[2]/form/div/div[1]/div[7]/div/div/div[1]/div/input')
    address.clear()
    address.send_keys(address)
    
    time.sleep(2)
    photo = driver.find_element(By.XPATH, value='/html/body/div[3]/div/div/div[2]/div/div[2]/form/div/div[2]/div/div/div/label')
    photo.click()
    
    
    input("Press Enter when you have completed")
    
    
makeLinkedInContact(exampleLink)
    