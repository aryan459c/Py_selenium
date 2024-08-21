from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Set up the WebDriver (replace 'chromedriver' with the path to your driver)
driver = webdriver.Chrome()

# Open the demoqa slider page
driver.get('https://demoqa.com/slider')

# Locate the slider element
slider = driver.find_element(By.XPATH, '//input[@type="range"]')

# Initialize ActionChains
actions = ActionChains(driver)

# Move the slider forward (right)
# Dragging the slider by an offset (e.g., 50 pixels to the right)
actions.click_and_hold(slider).move_by_offset(50, 0).release().perform()

# Optionally, get the value after moving the slider
slider_value = slider.get_attribute('value')
print(f"Slider value after moving forward: {slider_value}")

# Move the slider backward (left)
# Dragging the slider by an offset (e.g., -30 pixels to the left)
actions.click_and_hold(slider).move_by_offset(-30, 0).release().perform()

# Optionally, get the value after moving the slider
slider_value = slider.get_attribute('value')
print(f"Slider value after moving backward: {slider_value}")

# Close the browser
driver.quit()
