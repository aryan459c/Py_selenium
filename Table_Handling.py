import time
from selenium import webdriver
from selenium.webdriver.common.by import  By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

table=driver.find_element(By.XPATH,"(//table[@id='product'])[1]")
time.sleep(2)
rows=table.find_elements(By.TAG_NAME,"tr")


hedding=table.find_elements(By.TAG_NAME,"th")
for value in hedding:
    print(value.text)

"""for row in rows:
    print(row.text)"""


time.sleep(3)