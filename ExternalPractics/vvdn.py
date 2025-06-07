from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://google.com")
time.sleep(10)
var1 = driver.find_elements(By.XPATH, "//div[@id='SIvCob']/a")
for i in var1:
    print(i.text)
