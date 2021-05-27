from selenium import webdriver
from sys import platform
import os

class TestConfiguration:
    
    def get_driver(self):
        if platform == "osx":
            return webdriver.Chrome(
                os.path.join(os.getcwd(),
                    "driver","executable","chromedriver"))
        elif platform == "linux":
            return webdriver.Chrome(
                os.path.join(os.getcwd(),
                    "driver","executable","chromedriver"))