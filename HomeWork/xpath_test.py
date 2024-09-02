from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.nseindia.com/")
Action_Chain=ActionChains(driver)
elemen_maket_data=driver.find_element(By.XPATH,"//li/a[text()='Market Data']")
Action_Chain.move_to_element(elemen_maket_data).perform()
driver.find_element(By.XPATH,"//li/a[text()='Pre-Open Market']").click()