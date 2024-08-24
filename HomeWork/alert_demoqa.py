import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://demoqa.com/')
driver.maximize_window()

"""Click Element Button"""
driver.execute_script("window.scrollBy(0,500)")
driver.find_element(By.XPATH, "//div[@class='card-body'][1]").click()


"""Go to Alerts, Frame & Windows Element and Click"""
AlFrWd=driver.find_element(By.XPATH,"//div[text()='Alerts, Frame & Windows']")
driver.execute_script("arguments[0].scrollIntoView();",AlFrWd)
AlFrWd.click()

"""Handel Alert"""
driver.find_element(By.XPATH,"//li/span[text()='Alerts']").click()
driver.find_element(By.ID,"confirmButton").click()
time.sleep(2)
driver.switch_to.alert.accept()
print("Alert_Result: ",driver.find_element(By.ID,"confirmResult").text)
time.sleep(3)