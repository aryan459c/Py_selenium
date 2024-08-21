import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.automationtesting.in/FileUpload.html")
loc=driver.find_element(By.ID,"input-4")
loc.send_keys("C:\\Users\\AryaN\\Pictures\\sql-1024x536.jpg")
time.sleep(3)