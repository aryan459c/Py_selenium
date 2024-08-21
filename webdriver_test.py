from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
"""driver.find_element(By.CSS_SELECTOR,"#checkBoxOption3").click()
var1= driver.find_element(By.CSS_SELECTOR,"#checkBoxOption1").is_selected()"""

driver.find_element(By.CSS_SELECTOR,'input[value="radio3"]').click()
var1= driver.find_element(By.CSS_SELECTOR,'input[value="radio3"]').is_selected()

print(var1) #true
time.sleep(5)


