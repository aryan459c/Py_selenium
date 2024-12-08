from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import  time


# Connect Browser
driver=webdriver.Chrome()

# Navigate the Webpage
driver.get("https://www.naukri.com/")

# Maximize Window
driver.maximize_window()
Wait=WebDriverWait(driver,30)

# Click Login Button
driver.find_element(By.LINK_TEXT,"Login").click()
loginpagevarify=driver.find_element(By.XPATH,"//label[@class='label' and text()='Email ID / Username']").text
if loginpagevarify == "Email ID / Username":
    driver.find_element(By.XPATH,"//input[@placeholder='Enter your active Email ID / Username']").send_keys("sunilkumaharana01@gmail.com")
    driver.find_element(By.XPATH,"//input[@type='password']").send_keys("Aryan@7874")
    driver.find_element(By.XPATH,"//button[@type='submit']").click()
    Wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@placeholder='Enter keyword / designation / companies']")))
driver.find_element(By.XPATH,"r//input[@placeholder='Enter keyword / designation / companies']").send_keys("Automation Test Engineering, Selenium, Pytest")
