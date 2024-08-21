import time
from selenium import webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()
driver.get("https://www.w3schools.com/html/html5_draganddrop.asp")
driver.maximize_window()
driver.implicitly_wait(5)
action=ActionChains(driver)
source=driver.find_element(By.XPATH,"//img[@src='img_w3slogo.gif']")
destination=driver.find_element(By.XPATH,"//div[@id='div2']")
action.drag_and_drop(source,destination).perform()

time.sleep(5)