import os
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the WebDriver (replace 'chromedriver' with the path to your driver)
driver = webdriver.Chrome()

# Open the demoqa upload-download page
driver.get('https://demoqa.com/upload-download')

# Locate the upload button
upload_input = driver.find_element(By.ID, 'uploadFile')

# Specify the file path to upload (replace with your file path)
file_path = r'C:\Users\TREENETRA\Downloads\new_logo.png'

# Upload the file by sending the file path to the input element
upload_input.send_keys(file_path)

# (Optional) Fetch and print the uploaded file path displayed on the webpage
uploaded_file_path = driver.find_element(By.ID, 'uploadedFilePath').text
print(f"Uploaded file path: {uploaded_file_path}")

# Close the browser
driver.quit()