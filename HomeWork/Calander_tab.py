import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.get('D:/STUDY/Python/Selenium/index.html')
driver.maximize_window()
wait=WebDriverWait(driver,10)


# //td[@class='today']  #Today
today=driver.find_element(By.XPATH,'//td[contains(@class,"today")]')
print("Today",today.text)



# (//td[@class='today'])/preceding-sibling::td[1]   #Previous currentday
previous_day=driver.find_element(By.XPATH,"(//td[@class='today'])/preceding-sibling::td[1]")
print("Previous Date:",previous_day.text)


# (//td[@class='today'])/following-sibling::td[1]   #Nextdate Currentday

Tommarow=driver.find_element(By.XPATH,"(//td[@class='today'])/following-sibling::td[1]")
print("Tommarow",Tommarow.text)


# (//tbody[@id="calendar-body"]//td[text()])[position()>2 and position()<24]   Range 3 to 23 date
li_range=[]
for day in range(3,24):
    singlexpath=f"(//tbody[@id='calendar-body']//td[text()])[{day}]"
    f_element=driver.find_element(By.XPATH, singlexpath)
    d_data=int(f_element.text)
    li_range.append(d_data)
print(li_range)

# Goto Previous Month Using Click button
driver.find_element(By.XPATH,"(//h2[@id='month-year'])/preceding-sibling::button[@class='nav-button prev']").click()
time.sleep(2)

