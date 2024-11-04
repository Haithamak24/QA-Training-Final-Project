from selenium import webdriver

def get_driver(options=None):
    if options is None:
        options = webdriver.ChromeOptions()  
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    return driver
