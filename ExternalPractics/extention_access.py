from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

extension_path = "/path/to/unpacked/extension/"
options = Options()
options.add_argument(f"--load-extension={extension_path}")
driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com")
time.sleep(5)
driver.quit()
