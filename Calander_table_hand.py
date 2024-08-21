import time

from selenium import webdriver
from selenium.webdriver.common.by import  By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Datepicker.html")
driver.implicitly_wait(7)

driver.find_element(By.XPATH,"//input[@id='datepicker1']").click()
driver.find_element(By.XPATH,"(//td[@data-handler='selectDay'])[30]").click()
time.sleep(4)