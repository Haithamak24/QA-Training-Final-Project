import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.menu_icon = 'button#react-burger-menu-btn'
        self.logout_option = 'a#logout_sidebar_link'
        self.sort_dropdown = 'select.product_sort_container'
        self.product_list = 'div.inventory_item' 
        self.product_name_selector = 'div.inventory_item_name'
        self.product_price_selector = 'div.inventory_item_price' 
        self.product_elements = self.product_list  
    def logout(self):
        self.driver.find_element(By.CSS_SELECTOR, self.menu_icon).click()
        self.driver.find_element(By.CSS_SELECTOR, self.logout_option).click()

    def sort_products(self, option):
        dropdown = self.driver.find_element(By.CSS_SELECTOR, self.sort_dropdown)
        select = Select(dropdown)
        select.select_by_visible_text(option)

        time.sleep(2) 
        products = self.driver.find_elements(By.CSS_SELECTOR, self.product_name_selector)
        
        product_names = [product.text for product in products]

        if option == "Name (A to Z)":
            assert product_names == sorted(product_names), "Products are not sorted alphabetically (A to Z)."
        elif option == "Name (Z to A)":
            assert product_names == sorted(product_names, reverse=True), "Products are not sorted alphabetically (Z to A)."

    def get_product_price(self, product_element):
        price_element = product_element.find_element(By.CSS_SELECTOR, self.product_price_selector)
        return float(price_element.text.replace('$', '').strip())

    def click_random_product(self):
        time.sleep(2)  
        products = self.driver.find_elements(By.CSS_SELECTOR, self.product_list)
        
        if not products:
            print("No products found to click.")
            return
        
        random_index = random.randint(0, len(products) - 1)
        random_product = products[random_index]

        product_name = random_product.text
        try:
            random_product.click()
            time.sleep(2)  
        except Exception as e:
            print(f"Error clicking on product '{product_name}': {e}")
            raise
    def get_all_product_names(self):
        product_elements = self.driver.find_elements(By.CSS_SELECTOR, self.product_name_selector)
        return [product.text for product in product_elements]
    

    def click_product(self, product_name):
        products = self.driver.find_elements(By.CSS_SELECTOR, self.product_list)
        for product in products:
            if product_name in product.text:
                product.click()
                return  
        print(f"Product '{product_name}' not found.")
