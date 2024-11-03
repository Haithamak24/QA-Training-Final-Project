from selenium.webdriver.common.by import By
class ErrorPage:
    def __init__(self, driver):
        self.driver = driver
        self.error_message = 'h1' 
        
    def get_error_message(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.error_message).text
