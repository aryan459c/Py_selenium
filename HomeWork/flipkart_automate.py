from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()

url = 'https://www.flipkart.com/black-friday-sale-store?param=72922&s_kwcid=AL!739!3!676201929245!b!!g!!flipkart&gclsrc=aw.ds&&semcmpid=sem_8024046704_brand_exe_buyers_goog&gad_source=1&gclid=Cj0KCQiAo5u6BhDJARIsAAVoDWvS9buglx9k3P1chQB7ZgZ2sKJCDAwhZ4ZLLbuFGw65F0VP7kwxgwMaAqGLEALw_wcB'

driver.get(url)

search_bar = driver.find_element(By.XPATH,"//input[@name='q']")
search_bar.send_keys('Mobile',Keys.ENTER)

time.sleep(5)
click_samsung_check_box = driver.find_element(By.XPATH,"//div[text()='SAMSUNG']/preceding-sibling::div")
click_samsung_check_box.click()

time.sleep(5)

gb_select = driver.find_element(By.XPATH,"//div[text()='8 GB and Above']/preceding-sibling::div")
gb_select.click()

#how to check the ancher tag using tagname

'''a_tag_check = driver.find_elements(By.TAG_NAME,'a')
print(a_tag_check)
print(len(a_tag_check))'''

#link text and partial link text

# link text :- wants the static text mentioned in the a tag, and it want a perfect data

'''click_became_a_seller = driver.find_element(By.LINK_TEXT,"Become a Seller")
click_became_a_seller.click()'''

#partial text :- paritially coorrect the text

click_became_a_seller = driver.find_element(By.PARTIAL_LINK_TEXT,"Become")
click_became_a_seller.click()


time.sleep(5)
driver.close()