import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://greensshopping.com/")

action=ActionChains(driver)
wait=WebDriverWait(driver,7)
action.move_to_element(driver.find_element(By.LINK_TEXT,"FRUITS & VEGETABLES")).perform()
driver.find_element(By.LINK_TEXT, "FRUITS").click()
driver.find_element(By.XPATH,"//img[@alt='Water melon 1pcs']").click()
driver.find_element(By.XPATH,"(//*[@id='addbag'])[1]").click()
time.sleep(4)
driver.find_element(By.XPATH,"(//a[@href='https://greensshopping.com/en/cart'])[2]").click()
time.sleep(10)