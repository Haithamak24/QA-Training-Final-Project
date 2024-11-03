from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = 'input#user-name'
        self.password_field = 'input#password'
        self.login_button = 'input[type="submit"]'
        self.main_page_element = 'div#root'  # Using the unique element to identify the main page

    def login(self, username, password):
        self.driver.find_element(By.CSS_SELECTOR, self.username_field).send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, self.password_field).send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, self.login_button).click()

        # Assertion to ensure we are on the main page after login
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, self.main_page_element))
            )
            assert self.driver.find_element(By.CSS_SELECTOR, self.main_page_element).is_displayed(), "Main page not displayed"
            print("Login successful, main page is displayed.")
        except Exception as e:
            print("Login failed or main page did not load:", str(e))
            self.driver.quit()  
