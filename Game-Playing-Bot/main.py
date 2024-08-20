from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# bigCookie


def cookieMaster(timer:int):
    driver = webdriver.Chrome(options=chrome_options)
 
    driver.get("https://orteil.dashnet.org/cookieclicker/")    
    cookieBtn = driver.find_element(By.CSS_SELECTOR, value="#bigCookie")
    
    for _ in range(timer):
        cookieBtn.send_keys(Keys.ENTER)


print(cookieMaster(10))
    