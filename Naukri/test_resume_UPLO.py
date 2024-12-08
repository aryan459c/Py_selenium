import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# Test Configuration
USERNAME = "sunilkumaharana01@gmail.com"  # Replace with your Naukri.com username
PASSWORD = "Aryan@7874"  # Replace with your Naukri.com password
RESUME_PATH = "D:\AngryRider\RESUME WITH ALL INTERVIEW\PAT_Resume_sunil.pdf"  # Replace with the file path of your resume


@pytest.fixture(scope="class")
def setup_browser():
    """Fixture to initialize and clean up WebDriver."""
    driver = webdriver.Chrome()  # Make sure ChromeDriver is in PATH
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.mark.usefixtures("setup_browser")
class TestNaukriUpload:
    """Class to automate Naukri.com resume upload."""

    def test_login(self, setup_browser):
        """Log in to Naukri.com."""
        driver = setup_browser
        driver.get("https://www.naukri.com/")

        # Close popup if it appears
        try:
            popup = driver.find_element(By.CLASS_NAME, "crossIcon")
            popup.click()
        except:
            pass

        # Navigate to login
        driver.find_element(By.LINK_TEXT, "Login").click()
        time.sleep(2)

        # Enter credentials and log in
        driver.find_element(By.XPATH,"//input[@placeholder='Enter your active Email ID / Username']").send_keys(USERNAME)
        driver.find_element(By.XPATH,"//input[@type='password']").send_keys(PASSWORD)
        driver.find_element(By.XPATH, "//button[text()='Login']").click()
        time.sleep(5)

    def test_upload_resume(self, setup_browser):
        """Upload resume on Naukri.com."""
        driver = setup_browser

        # Navigate to profile section
        driver.find_element(By.LINK_TEXT, "UPDATE PROFILE").click()
        time.sleep(5)

        # Locate and upload resume
        upload_button = driver.find_element(By.XPATH, "//input[@type='file' and @name='uploadCV']")
        upload_button.send_keys(RESUME_PATH)
        time.sleep(3)

        # Verify upload success
        success_message = driver.find_element(By.XPATH, "//div[contains(text(), 'successfully uploaded')]")
        assert "successfully uploaded" in success_message.text, "Resume upload failed"

# To run the tests, use the command: pytest -v test_naukri_resume_upload.py
