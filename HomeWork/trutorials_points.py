from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os

name = "Aryan Maharana"
email = "sunilkumaharana459@gmail.com"
mob = "9114590459"
subjects = "PAT"
pic_path = os.path.abspath(r"C:\Users\sunil\Desktop\FinalIMP\instaart.jpg")
Current_add = "At-xyg, po- abc"

def reg_form(name, email, mob, subjects, pic_path, Current_add):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
    wait = WebDriverWait(driver, 10)
    name_input = wait.until(EC.presence_of_element_located((By.ID, "name")))
    name_input.clear()
    name_input.send_keys(name)
    email_input = driver.find_element(By.ID, "email")
    email_input.clear()
    email_input.send_keys(email)
    gender_radio = driver.find_element(By.ID, "gender")
    gender_radio.click()
    mobile_input = driver.find_element(By.ID, "mobile")
    mobile_input.clear()
    mobile_input.send_keys(mob)
    subjects_input = driver.find_element(By.ID, "subjects")
    subjects_input.clear()
    subjects_input.send_keys(subjects)
    subjects_input.send_keys(Keys.ENTER)
    picture_input = driver.find_element(By.ID, "picture")
    picture_input.send_keys(pic_path)
    address_textarea = driver.find_element(By.XPATH, "//textarea[@id='picture']")
    address_textarea.clear()
    address_textarea.send_keys(Current_add)
    time.sleep(10)
    print("Page title:", driver.title)
    driver.quit()

reg_form(name, email, mob, subjects, pic_path, Current_add)