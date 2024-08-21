from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element(By.NAME,"enter-name").send_keys("Sunil")
driver.find_element(By.ID,"alertbtn").click()
time.sleep(2)
alert_handel=driver.switch_to.alert
print(alert_handel.text)
alert_handel.accept()
# alert_handel.dismiss()


time.sleep(2)