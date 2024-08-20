from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)

driver.get("https://secure-retreat-92358.herokuapp.com/")


# Grab lineedit and submit data
fNameLineEdit = driver.find_element(By.NAME, value="fName")
fNameLineEdit.send_keys("Azura")

lNameLineEdit = driver.find_element(By.NAME, value="lName")
lNameLineEdit.send_keys("Blue")

emailLineEdit = driver.find_element(By.NAME, value="email")
emailLineEdit.send_keys("email@email.com")

btn = driver.find_element(By.CLASS_NAME, value="btn")
btn.send_keys(Keys.ENTER)

driver.quit()