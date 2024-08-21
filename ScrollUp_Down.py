import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(3)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
driver.execute_script("window.scrollBy(0,600)")
element= driver.find_element(By.ID,"confirmbtn")
driver.execute_script("arguments[0].scrollIntoView();",element)
time.sleep(2)
driver.execute_script("window.scrollTo(0,0)")
time.sleep(3)
driver.close()

# for opening new window
# driver.execute_script("window.open('','_blank')")
# time.sleep(1)
# driver.execute_script("window.open('https://www.facebook.com/')")
# time.sleep(3)
# driver.close()