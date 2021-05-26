from selenium import webdriver


class NewBugPage(BasePage): 
    driver = webdriver.Chrome()
    def fill_form(title, description): 
        driver.find_element_by_name('Title').send_keys(title)
        driver.find_element_by_name('Description').send_keys(description)

    def submit_new_bug(): 
       driver.find_element_by_name('Next').click()

    def cancel_bug_submission():
        driver.find_element_by_name('Cancel').click()