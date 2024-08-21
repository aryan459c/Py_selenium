import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import  By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
wait=WebDriverWait(driver,7)
driver.find_element(By.ID,"autocomplete").send_keys("ind")
li_country=wait.until(EC.visibility_of_all_elements_located((By.XPATH,"//ul/li[@class='ui-menu-item']")))
for country in li_country:
    if country.text == "India":
        country.click()
        break

time.sleep(4)

