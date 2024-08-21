import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# # for the checkbox option
var1=driver.find_element(By.CSS_SELECTOR,"#checkBoxOption3").is_selected()
print(var1)   # False
driver.find_element(By.CSS_SELECTOR,"#checkBoxOption3").click()
time.sleep(3)
var2=driver.find_element(By.CSS_SELECTOR,"#checkBoxOption3").is_selected()
print(var2) #True
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"#checkBoxOption1").click()
time.sleep(3)
var3= driver.find_element(By.CSS_SELECTOR,"#checkBoxOption1").is_selected()
print("this is last selected element of option 1",var3) #True
print("This is first selected element of option 3",driver.find_element(By.CSS_SELECTOR,"#checkBoxOption3").is_selected()) # True

# for the radio buttons
radiobutton1=driver.find_element(By.CSS_SELECTOR,"input[value='radio1']")
print("before selection of radio button 1",radiobutton1.is_selected())  # False
time.sleep(2)
radiobutton1.click()
time.sleep(2)
print("after selection of radio button 1",radiobutton1.is_selected()) #True
time.sleep(3)
radiobutton3=driver.find_element(By.CSS_SELECTOR,"input[value='radio3']")
print("before selecting the radio button 3 value is",radiobutton3.is_selected()) # False
radiobutton3.click()
time.sleep(2)
print("after selecting radio button 3 ",radiobutton3.is_selected()) # True
print("after selecting radio button 3 value of radion button 1",radiobutton1.is_selected()) # False