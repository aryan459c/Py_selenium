from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Set up the WebDriver (replace 'chromedriver' with the path to your driver)
driver = webdriver.Chrome()

# Open the demoqa draggable page
driver.get('https://demoqa.com/dragabble')

# Locate the draggable element
draggable = driver.find_element(By.ID, 'dragBox')

# Initialize ActionChains
actions = ActionChains(driver)

# Define the specific position to drag to (e.g., 100 pixels right and 50 pixels down)
x_offset = 100
y_offset = 50

# Drag the element to the specific position
actions.drag_and_drop_by_offset(draggable, x_offset, y_offset).perform()

# Close the browser
driver.quit()
