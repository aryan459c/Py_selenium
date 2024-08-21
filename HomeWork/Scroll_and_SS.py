from selenium import webdriver
import time

# Set up the WebDriver (replace 'chromedriver' with the path to your driver)
driver = webdriver.Chrome()

# Open a webpage (for example, demoqa.com)
driver.get('https://demoqa.com')

# Scroll down the page by a specified amount (e.g., 1000 pixels)
driver.execute_script("window.scrollBy(0, 1000);")

# Wait to observe the scroll action
time.sleep(2)

# Scroll back up the page
driver.execute_script("window.scrollBy(0, -1000);")

# Wait for the action to complete
time.sleep(2)

# Take a screenshot and save it to a file
screenshot_path = 'scroll.png'
driver.save_screenshot(screenshot_path)
print(f"Screenshot saved to {screenshot_path}")

# Close the browser
driver.quit()
