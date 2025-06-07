import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Replace with your credentials and file path
USERNAME = "sunilkumaharana02@gmail.com"
PASSWORD = "Aryan@7874"
RESUME_PATH = r"C:\Users\sunil\Desktop\Sunil_Kumar_Maharana_PythonAutomationTester.pdf"
RESUME_STATUS = "Update_resume"

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Open Naukri website
driver.get("https://www.naukri.com/")

# Click on Login button
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Login"))).click()

# Enter login credentials
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[placeholder="Enter your active Email ID / Username"]'))
).send_keys(USERNAME)
driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter your password"]').send_keys(PASSWORD)
driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

# ✅ Wait until login is successful
WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, '//a[contains(@href, "mnjuser/profile")]')))

# ✅ Navigate to Profile page
driver.get("https://www.naukri.com/mnjuser/profile")

try:
    # ✅ Check if delete button exists
    delete_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'i[data-title="delete-resume"]'))
    )
    print("🔹 Old resume found. Deleting...")

    # Click on delete button
    delete_button.click()

    # ✅ Wait for confirmation popup and confirm deletion
    confirm_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[@class='lightbox model_open flipOpen']//button[@class='btn-dark-ot']")
        )
    )
    confirm_button.click()

    print("✅ Old resume deleted successfully.")
    time.sleep(2)  # Wait for deletion to complete
    driver.refresh()  # let reload the page

except TimeoutException:
    print("🔸 No existing resume found. Proceeding to upload.")

# ✅ Upload new resume
try:
    upload_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[id="attachCV"]'))
    )
    # Upload file
    upload_element.send_keys(RESUME_PATH)
    print("✅ Resume uploaded successfully!")

except (TimeoutException, NoSuchElementException) as e:
    print("❌ Resume upload failed!")
    print(f"⚠️ Error: {e}")

# Quit driver
time.sleep(3)  # Allow time for processing
driver.quit()
