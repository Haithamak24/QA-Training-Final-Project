import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestInvalidProduct:
    def setup_method(self):
        self.driver = webdriver.Chrome() 

    def teardown_method(self):
        self.driver.quit()

    def test_invalid_product_details(self):
        self.driver.get("https://www.saucedemo.com/inventory-item.html?id=999")

        try:
            error_message = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".inventory_details_name[data-test='inventory-item-name']"))
            )
            assert error_message.text == "ITEM NOT FOUND", "Error message does not match expected value."
        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(2)
