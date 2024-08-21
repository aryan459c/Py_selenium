import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.current_window_handle)
driver.find_element(By.LINK_TEXT,"Open Tab").click()
time.sleep(3)
driver.find_element(By.ID,"openwindow").click()
all_windows= driver.window_handles
driver.switch_to.window(all_windows[1])
driver.find_element(By.LINK_TEXT,"Access all our Courses").click()
time.sleep(4)
driver.switch_to.window(all_windows[0])
driver.find_element(By.ID,"checkBoxOption2").click()
time.sleep(4)

driver.switch_to.window(all_windows[2])
time.sleep(2)
driver.find_element(By.LINK_TEXT,"Access all our Courses").click()
time.sleep(3)