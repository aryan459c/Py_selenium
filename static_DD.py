from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
opti=driver.find_element(By.TAG_NAME,"select")
Select(opti).select_by_index(1)
# Select(opti).select_by_value("option2")
# Select(opti).select_by_visible_text("Option3")



time.sleep(5)