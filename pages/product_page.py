import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.menu_icon = 'button#react-burger-menu-btn'
        self.logout_option = 'a#logout_sidebar_link'
        self.sort_dropdown = 'select.product_sort_container'
        
    def logout(self):
        self.driver.find_element(By.CSS_SELECTOR, self.menu_icon).click()
        self.driver.find_element(By.CSS_SELECTOR, self.logout_option).click()
        
    def sort_products(self, option):
        dropdown = self.driver.find_element(By.CSS_SELECTOR, self.sort_dropdown)
        select = Select(dropdown)  
        select.select_by_visible_text(option)

    def click_product(self, product_name):
        """Click on a product by its name."""
        try:
            product_element = self.driver.find_element(By.XPATH, f"//div[text()='{product_name}']")
            product_element.click()
            time.sleep(2)  
        except Exception as e:
            print(f"Error clicking on product '{product_name}': {e}")
            raise
