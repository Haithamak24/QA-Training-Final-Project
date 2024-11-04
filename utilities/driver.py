from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import logging

def get_driver(options=None):
    if options is None:
        options = webdriver.ChromeOptions()
    
    options.add_argument('--headless')  
    options.add_argument('--no-sandbox')  
    options.add_argument('--disable-dev-shm-usage')  
    options.add_argument('--disable-gpu')  # Optional, for Windows

    try:
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(10)
        return driver
    except WebDriverException as e:
        logging.error("Failed to initialize WebDriver: %s", e)
        raise
