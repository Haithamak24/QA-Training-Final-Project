import pytest
import time
from selenium.webdriver.common.by import By
from utilities.driver import get_driver
from pages.login_page import LoginPage
from pages.product_page import ProductPage

class TestLogout:
    @pytest.fixture
    def setup(self):
        self.driver = get_driver()
        self.driver.get("https://www.saucedemo.com/")
        self.login_page = LoginPage(self.driver)
        self.login_page.login("standard_user", "secret_sauce")
        time.sleep(2)
        yield
        self.driver.quit()

    def test_logout(self, setup):
        product_page = ProductPage(self.driver)
        product_page.logout()
        assert self.driver.current_url == "https://www.saucedemo.com/"
        time.sleep(2)
