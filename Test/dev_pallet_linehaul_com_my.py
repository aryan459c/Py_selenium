from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://dev.pallet.linehaul.com.my/login")

driver.find_element(By.LINK_TEXT, "Register here").click()
time.sleep(4)
driver.find_element(By.XPATH, "//div[contains(text(),'I want to place an order')]").click()
time.sleep(4)
driver.find_element(By.XPATH, "//button[contains(text(),'Personal Customer')]").click()
time.sleep(4)
driver.find_element(By.NAME, "name").send_keys("Roshan")
driver.find_element(By.NAME, "email").send_keys("roshan@gmail.com")
driver.find_element(By.NAME, "phone").send_keys("6967686565")
driver.find_element(By.NAME, "ic").send_keys("79676")
driver.find_element(By.NAME, "postcode").send_keys("760001")
driver.find_element(By.NAME, "address").send_keys("address")
driver.find_element(By.CLASS_NAME, 'css-13cymwt-control').click()
time.sleep(10)
driver.find_element(By.XPATH, "//input[@type='file']").send_keys(
    r"D:\STUDY\Python\pycharm\Selenium_pro\Test\Screenshot 2024-12-28 150504.png")

driver.find_element(By.NAME, "bankName").send_keys("Bankname")
driver.find_element(By.NAME, "beneficiaryName").send_keys("Benificiary")
driver.find_element(By.NAME, "bankAccount").send_keys("Bank A/c")
driver.find_element(By.XPATH, '//input[@type="checkbox"]').click()
time.sleep(20)
