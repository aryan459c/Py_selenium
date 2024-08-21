from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element(By.ID,"autocomplete").send_keys("ind")
time.sleep(3)
li_country=driver.find_elements(By.XPATH,"//ul/li[@class='ui-menu-item']")
for country in li_country:
    if country.text == "India":
        country.click()
        break

time.sleep(5)