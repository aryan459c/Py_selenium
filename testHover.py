import time
from selenium import webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()
driver.get("https://flipkart.com")
driver.maximize_window()
action=ActionChains(driver)
ele=driver.find_element(By.XPATH,"//input[@name='q']")
action.context_click(ele).perform()

time.sleep(4)