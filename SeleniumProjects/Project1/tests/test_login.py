import pytest
from Selenium_pro.SeleniumProjects.Project1.config.config import Config
from Selenium_pro.SeleniumProjects.Project1.pages.login_page import LoginPage

def test_valid_login(setup_browser):
    driver = setup_browser
    login_page = LoginPage(driver)

    # Load the login page
    login_page.load_page(Config.BASE_URL)

    # Perform login
    login_page.enter_username(Config.USERNAME)
    login_page.enter_password(Config.PASSWORD)
    login_page.click_login()

    # Assert the user is redirected to the dashboard
    assert "dashboard" in driver.current_url, "Login failed or redirection incorrect"
