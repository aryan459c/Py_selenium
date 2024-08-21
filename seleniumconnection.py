import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://facebook.com")
"""driver.find_element(By.CLASS_NAME,"btnLogin-popup").click()
driver.find_element(By.NAME,"email").send_keys("sunilweb143@gmail.com")
driver.find_element(By.NAME,"password").send_keys("AryaN")
driver.find_element(By.CLASS_NAME,"btn").click()"""
time.sleep(20)
driver.close()