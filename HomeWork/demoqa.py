from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver=webdriver.Chrome()
driver.get("https://demoqa.com/")
driver.maximize_window()

print('\n -------------------------\n')

driver.execute_script("window.scrollBy(0,500)")
driver.find_element(By.XPATH, "//div[@class='card-body'][1]").click()
li_element=driver.find_elements(By.XPATH,"//div[@class='element-list collapse show']/ul[@class='menu-list']")
for i in li_element:
    print (i.text)
driver.find_element(By.ID,"item-0").click()
uname="Aryan Maharana"
uemail="aryan@info.com"
ucAdd="ABC"
upAdd="XYZ"

print('\n -------------------------\n')

driver.find_element(By.ID,"userName").send_keys(uname)
time.sleep(2)
driver.find_element(By.ID,"userEmail").send_keys(uemail)
time.sleep(2)
driver.find_element(By.ID,"currentAddress").send_keys(ucAdd)
time.sleep(2)
driver.find_element(By.ID,"permanentAddress").send_keys(upAdd)
element= driver.find_element(By.ID,"submit")
driver.execute_script("arguments[0].scrollIntoView();",element)
time.sleep(2)
element.click()
time.sleep(2)


print('\n -------------------------\n')


name=driver.find_element(By.XPATH,"//p[@id='name']").text
if name == 'Name:'+uname:
    print('name is matched')
else:print('name is not match')
email=driver.find_element(By.XPATH,"//p[@id='email']").text
if email == 'Email:'+uemail:
    print('Email is matched')
else:print('Email is not match')
currentAddress=driver.find_element(By.XPATH,"//p[@id='currentAddress']").text
if currentAddress == 'Current Address :'+ucAdd:
    print('currentAddress is matched')
else:print('currentAddress is not match')
permanentAddress=driver.find_element(By.XPATH,"//p[@id='permanentAddress']").text
if permanentAddress == 'Permananet Address :'+upAdd:
    print('permanentAddress is matched')
else:print('permanentAddress is not match')

print('\n -------------------------\n')

AlFrWd=driver.find_element(By.XPATH,"//div[text()='Alerts, Frame & Windows']")
driver.execute_script("arguments[0].scrollIntoView();",AlFrWd)
AlFrWd.click()

time.sleep(4)
driver.find_element(By.XPATH,"//li/span[text()='Frames']").click()
frame1=driver.find_element(By.ID,"frame1")
driver.execute_script("arguments[0].scrollIntoView()",frame1)
driver.switch_to.frame("frame1")
print("Frame1 : ",driver.find_element(By.ID,"sampleHeading").text)
driver.switch_to.parent_frame()
driver.switch_to.frame("frame2")
print("Frame2 : ",driver.find_element(By.ID,"sampleHeading").text)
driver.switch_to.parent_frame()
time.sleep(3)


print('\n -------------------------\n')


driver.find_element(By.XPATH,"//li/span[text()='Alerts']").click()
driver.find_element(By.ID,"confirmButton").click()
time.sleep(2)
driver.switch_to.alert.accept()
print("Alert_Result: ",driver.find_element(By.ID,"confirmResult").text)
time.sleep(3)

print('\n -------------------------\n')

driver.find_element(By.XPATH,"//li/span[text()='Browser Windows']").click()
driver.find_element(By.ID,"tabButton").click()
time.sleep(3)
all_windows=driver.window_handles
driver.switch_to.window(all_windows[1])
print('NewTab:',driver.find_element(By.ID,"sampleHeading").text)
time.sleep(3)

print('\n -------------------------\n')

driver.switch_to.window(all_windows[0])
print("Context Menu")
time.sleep(10)