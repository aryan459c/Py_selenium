from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.getfishtank.com/")
lists=driver.find_elements(By.XPATH,"//html")
for i in lists:
    print(i.text)