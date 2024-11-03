import pytest
import time 
from utilities.driver import get_driver
from pages.login_page import LoginPage
from pages.product_page import ProductPage

class TestViewProduct:
    @pytest.fixture
    def setup(self):
        self.driver = get_driver()
        self.driver.get("https://www.saucedemo.com/")
        self.login_page = LoginPage(self.driver)
        self.login_page.login("standard_user", "secret_sauce")
        time.sleep(2) 
        yield
        self.driver.quit()

    def test_view_product_details(self, setup):
        time.sleep(2) 
        product_page = ProductPage(self.driver)
        product_page.click_product("Sauce Labs Backpack")

        assert "Sauce Labs Backpack" in self.driver.page_source, "Product name is not displayed on the product page."

