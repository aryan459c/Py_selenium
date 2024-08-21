from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
time.sleep(2)
driver.switch_to.frame("courses-iframe") #Switch to Iframe Screen or Window
value=driver.find_element(By.XPATH,"//h2/span")
print(value.text)
driver.switch_to.parent_frame() #Switch to Main Page or parent frame
time.sleep(2)
driver.switch_to.default_content() #When we are in child window or tab return to Main Page use "default_cotent()'
