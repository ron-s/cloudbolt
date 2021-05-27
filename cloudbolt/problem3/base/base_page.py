from selenium import webdriver

base_url='https://bugs.info:4000/api/v1/bug'

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 60

    def navigate_to_url(self):
        self.driver.get(base_url)