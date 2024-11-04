import pytest
from selenium.webdriver.common.by import By
from utilities.driver import get_driver
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from selenium.webdriver.chrome.options import Options

class TestSorting:
    @pytest.fixture(scope="function")
    def setup(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        self.driver = get_driver(options=chrome_options)
        self.driver.get("https://www.saucedemo.com/")
        self.login_page = LoginPage(self.driver)
        self.login_page.login("standard_user", "secret_sauce")
        
        yield ProductPage(self.driver)
        self.driver.quit()

    def test_sort_name_a_to_z(self, setup):
        product_page = setup
        product_page.sort_products("Name (A to Z)")

        product_elements = self.driver.find_elements(By.CSS_SELECTOR, product_page.product_elements)
        product_names = [product.text for product in product_elements]

        assert product_names == sorted(product_names), "Products are not sorted correctly by name A to Z."

    def test_sort_name_z_to_a(self, setup):
        product_page = setup
        product_page.sort_products("Name (Z to A)")
        
        product_elements = self.driver.find_elements(By.CSS_SELECTOR, product_page.product_elements)
        product_names = [product.text for product in product_elements]

        assert product_names == sorted(product_names, reverse=True), "Products are not sorted correctly by name Z to A."

    def test_sort_price_low_to_high(self, setup):
        product_page = setup
        product_page.sort_products("Price (low to high)")

        product_elements = self.driver.find_elements(By.CSS_SELECTOR, product_page.product_elements)
        prices = [product_page.get_product_price(product) for product in product_elements]

        assert prices == sorted(prices), "Products are not sorted correctly by price low to high."

    def test_sort_price_high_to_low(self, setup):
        product_page = setup
        product_page.sort_products("Price (high to low)")

        product_elements = self.driver.find_elements(By.CSS_SELECTOR, product_page.product_elements)
        prices = [product_page.get_product_price(product) for product in product_elements]

        assert prices == sorted(prices, reverse=True), "Products are not sorted correctly by price high to low."
