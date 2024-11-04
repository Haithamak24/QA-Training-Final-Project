import pytest
from selenium.webdriver.common.by import By
from utilities.driver import get_driver
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestViewProduct:
    @pytest.fixture
    def setup(self):
        self.driver = get_driver()
        self.driver.get("https://www.saucedemo.com/")
        self.login_page = LoginPage(self.driver)
        self.login_page.login("standard_user", "secret_sauce")
        
        yield self.driver 
        self.driver.quit()

    def test_view_product_details(self, setup):
        product_page = ProductPage(setup)

        # Click on the product
        product_page.click_product("Sauce Labs Backpack")

        print(f"Current URL after clicking product: {setup.current_url}")
        
        try:
            WebDriverWait(setup, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "div.inventory_details_name"))
            )
        except Exception as e:
            print(f"Error waiting for product details: {e}")
            print(setup.page_source)  

        assert "Sauce Labs Backpack" in setup.page_source, "Product name is not displayed on the product page."
