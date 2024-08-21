from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
# driver.execute_script("window.open('','_blank')") Open a new Blank Window
driver.execute_script("window.open('https://fecebook.com')") # Open New facebook Window
time.sleep(4)
driver.close()



