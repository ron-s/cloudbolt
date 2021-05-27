from selenium import webdriver
from base_page import BasePage
import pytest


class NewBugPage(BasePage):
     
    driver = webdriver.Chrome()
    driver.maximize_window()
    def fill_form(title, description): 
        driver.find_element_by_name('Title').send_keys(title)
        driver.find_element_by_name('Description').send_keys(description)

    def submit_new_bug(): 
        driver.find_element_by_name('Next').click()

    def cancel_bug_submission():
        driver.find_element_by_name('Cancel').click()