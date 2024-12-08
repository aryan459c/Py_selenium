from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set up Chrome WebDriver with options
options = Options()
options.add_argument("--start-maximized")


try:
    # Initialize the WebDriver
    driver = webdriver.Chrome( options=options)

    # Open multiple tabs/windows for demonstration
    driver.get("https://www.google.com")  # Current window
    driver.execute_script("window.open('https://www.python.org', '_blank');")  # Open new tab
    driver.execute_script("window.open('https://www.selenium.dev', '_blank');")  # Open another tab

    # Get the current window handle
    current_window = driver.current_window_handle
    print(f"Current window handle: {current_window}")

    # Get all window handles
    all_windows = driver.window_handles
    print(f"All windows before closing: {all_windows}")

    # Close all windows except the current one
    for window in all_windows:
        if window != current_window:
            driver.switch_to.window(window)
            driver.close()
            print(f"Closed window handle: {window}")

    # Switch back to the current window
    driver.switch_to.window(current_window)
    print("Focused back on the current window.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Optionally, quit the driver (close all windows if needed)
    # driver.quit()
    print("Program finished.")
