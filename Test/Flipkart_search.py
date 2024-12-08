from selenium import webdriver
import  time

driver=webdriver.Chrome()
driver.get('https://www.flipkart.com/')
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element("//input[@name='q']").send_keys("phone")
time.sleep(3)

