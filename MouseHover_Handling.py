from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
Action_Chain=ActionChains(driver)
driver.maximize_window()
elemen=driver.find_element(By.ID,"mousehover")
Action_Chain.move_to_element(elemen).perform()
time.sleep(3)
driver.find_element(By.LINK_TEXT,"Reload").click()
time.sleep(3)

driver.close()