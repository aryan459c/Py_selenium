from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
print(driver.current_window_handle) #showing Current window id
driver.find_element(By.LINK_TEXT,"Open Tab").click()
time.sleep(3)
all_win=driver.window_handles  #windows in List Form
driver.switch_to.window(all_win[1]) #widows and tab store in index form we can call index wise
driver.find_element(By.PARTIAL_LINK_TEXT,"Access all our Courses").click()
time.sleep(2)
driver.switch_to.window(all_win[0])
time.sleep(2)