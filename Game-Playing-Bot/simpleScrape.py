from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)

driver.get(url="https://www.python.org/")

# firstEvent = driver.find_element(By.XPATH, value="//*[@id='content']/div/section/div[2]/div[2]/div/ul/li[1]/a")

times = []
events = []
for i in range(5):
    times.append(driver.find_element(By.XPATH, value=f"//*[@id='content']/div/section/div[2]/div[2]/div/ul/li[{i+1}]/time"))
    events.append(driver.find_element(By.XPATH, value=f"//*[@id='content']/div/section/div[2]/div[2]/div/ul/li[{i+1}]/a"))

for i in range(len(times)):
    print(times[i].text, " ", events[i].text)
 
pythonEvents = {}

for i in range(5):
    pythonEvents[i] = {'time', times[i].text,
                       'name', events[i].text}
       

driver.quit()



print(pythonEvents)