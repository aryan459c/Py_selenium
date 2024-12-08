from selenium import webdriver as WB
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver=WB.Chrome()
driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.XPATH,"//a[@data-nav-role='signin' and @data-nav-ref='nav_ya_signin']").click()

driver.find_element(By.ID,"ap_email").send_keys("sunilweb143@gmail.com")
driver.implicitly_wait(10)
wait=WebDriverWait(driver,7)
driver.find_element(By.ID,'continue').click()
wait.until(EC.visibility_of_all_elements_located((By.ID,'signInSubmit')))
driver.find_element(By.ID,"ap_password").send_keys("JK@7874")
driver.find_element(By.ID,'signInSubmit').click()
if wait.until(EC.visibility_of(By.XPATH,"//input[@aria-labelledby='cvf-submit-otp-button-announce']")):
    time.sleep(10)
    otp_num = driver.find_element(By.XPATH, "//input[@id='input-box-otp']").get_attribute("value")
    if len(otp_num) == 6:
        driver.find_element(By.XPATH, "//input[@aria-labelledby='cvf-submit-otp-button-announce']").click()
        print("Successfully LogedIn")
    else:
        print("Enterd Otp Length is not morethan 6 digit and  not lessthan 6 digit ")

