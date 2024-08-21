import base64
import time
from selenium import webdriver
from selenium.webdriver.support import wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import  By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://google.com")
# driver.save_screenshot("practics.png")  #For ScreenShot Same Location Only Give Photoname.extention
# driver.save_screenshot("C:\\Users\\AryaN\\Desktop\\photo.png")
# driver.get_screenshot_as_file("C:\\Users\\AryaN\\Desktop\\photo.png")
"""ss=driver.get_screenshot_as_png()
with open("C:\\Users\\AryaN\\Desktop\\photo.png","wb") as file:
    file.write(screenshot)
    file.close()"""


"""screens=driver.get_screenshot_as_base64()
print(screens)
with open("C:\\Users\\AryaN\\Desktop\\photo.png","wb") as file:
    file.write(base64.decode(screenshot))
    file.close()"""


time.sleep(3)