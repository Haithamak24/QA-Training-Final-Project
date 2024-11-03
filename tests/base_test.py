import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseTest:
    @pytest.fixture(autouse=True)
    def setup(self):
        # Setup code: e.g., starting the WebDriver
        self.driver = webdriver.Chrome()  # or whichever driver you're using
        yield  # This allows the test to run
        # Teardown code: e.g., quitting the WebDriver
        self.driver.quit()

    def navigate_to(self, url):
        """Navigate to a specified URL and wait for the page to load."""
        self.driver.get(url)
        # Optionally wait for the page to load completely
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))  # Adjust as needed
