from selenium import webdriver


class NewBugPage(BasePage): 
    driver = webdriver.Chrome()
    def fill_form(title:str, description:str): 
        driver.find_element_by_name("Title").send_keys("This is a unique but title")
        driver.find_element_by_name("Description").send_keys("This is some unique bug description")

    def submit_new_bug(): 
       driver.find_element_by_name("submit").click()

    def cancel_bug_submission():
        driver.find_element_by_name("cancel").click()