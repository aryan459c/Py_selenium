from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
time.sleep(3)
"""driver.execute_script("window.scrollTo(0,document.body.scrollHeight)") # goto current page end position
time.sleep(2)"""
driver.execute_script("window.scrollBy(0,600)")
time.sleep(2)
driver.execute_script("window.scrollTo(0,0)") # Goto Bottom to Top
time.sleep(2)


driver.close()





