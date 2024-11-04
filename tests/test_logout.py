import pytest
import time
from selenium.webdriver.common.by import By
from utilities.driver import get_driver
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from selenium.webdriver.chrome.options import Options

class TestLogout:
    @pytest.fixture
    def setup(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        self.driver = get_driver(options=chrome_options)
        self.driver.get("https://www.saucedemo.com/")
        
        # Perform login
        self.login_page = LoginPage(self.driver)
        self.login_page.login("standard_user", "secret_sauce")
        
        time.sleep(2)
        yield
        self.driver.quit()

    def test_logout(self, setup):
        # Perform logout and verify
        product_page = ProductPage(self.driver)
        product_page.logout()
        assert self.driver.current_url == "https://www.saucedemo.com/"
        time.sleep(2)  
