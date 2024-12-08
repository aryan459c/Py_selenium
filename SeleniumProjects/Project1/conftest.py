import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def setup_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
