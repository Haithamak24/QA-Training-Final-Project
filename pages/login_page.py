from selenium.webdriver.common.by import By
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = 'input#user-name'
        self.password_field = 'input#password'
        self.login_button = 'input[type="submit"]'
        
    def login(self, username, password):
        self.driver.find_element(By.CSS_SELECTOR, self.username_field).send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, self.password_field).send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, self.login_button).click()


