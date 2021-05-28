from selenium import webdriver
from Base.base_page import BasePage
import pytest


class NewBugPage(BasePage):

    driver = webdriver.Chrome(self)

    def fill_form(title, description): 
        driver.find_element_by_name('Title').clear()
        driver.find_element_by_name('Title').send_keys(title)
        driver.find_element_by_name('Description').clear()
        driver.find_element_by_name('Description').send_keys(description)

    def submit_new_bug(): 
        driver.find_element_by_name('Next').click()

    def cancel_bug_submission():
        driver.find_element_by_name('Cancel').click()
    
    def fill_title_only(title):
        driver.find_element_by_name('Title').clear()
        driver.find_element_by_name('Title').send_keys(title)
    
    def fill_description_only(description):
        driver.find_element_by_name('Description').clear()
        driver.find_element_by_name('Description').send_keys(description)