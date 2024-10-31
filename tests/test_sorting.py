import pytest
import time 
from utilities.driver import get_driver
from pages.login_page import LoginPage
from pages.product_page import ProductPage

class TestSorting:
    @pytest.fixture
    def setup(self):
        self.driver = get_driver()
        self.driver.get("https://www.saucedemo.com/")
        self.login_page = LoginPage(self.driver)
        self.login_page.login("standard_user", "secret_sauce")
        time.sleep(2)
        yield
        self.driver.quit()

    def test_sort_name_a_to_z(self, setup):
        product_page = ProductPage(self.driver)
        product_page.sort_products("Name (A to Z)")
        time.sleep(2)

    def test_sort_name_z_to_a(self, setup):
        product_page = ProductPage(self.driver)
        product_page.sort_products("Name (Z to A)")
        time.sleep(2)

    def test_sort_price_low_to_high(self, setup):
        product_page = ProductPage(self.driver)
        product_page.sort_products("Price (low to high)")
        time.sleep(2)

    def test_sort_price_high_to_low(self, setup):
        product_page = ProductPage(self.driver)
        product_page.sort_products("Price (high to low)")
        time.sleep(2)

