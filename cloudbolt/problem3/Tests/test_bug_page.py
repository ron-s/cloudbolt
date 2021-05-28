from Pages.bug_page import NewBugPage
from Base.base import Base
import pytest

class TestNewBugPage(Base):

    def test_bug_submittion_successful(self):
        """
        Verify you can submit a bug using title and description 
        and verify you see a success message.
        """
        title = "app is crashing after pressing submit."
        description = "without filling in any text entries pressing submit crashes the app."
        driver = self.driver
        new_bug = NewBugPage(driver)
        new_bug.fill_form(title, description)
        response = new_bug.submit_new_bug()
        # verify 200 request status code
        assert response.status_code == 200
        # I'm making assumptions here because there's no info regarding
        # elements on a successful submission page 
        assert "title" in response
        assert "description" in response
        assert "bug id" in response
        assert "bug id" in response != 1234

    def test_invalid_bug_submission(self):
        """
        Verify you can't submit a bug with invalid title and description 
        """
        title = 123445656
        description = 908765443321
        driver = self.driver
        new_bug = NewBugPage(driver)
        new_bug.fill_form(title, description)
        response = new_bug.submit_new_bug()
        # verify you don't receive a 200 request status code
        assert response.status_code != 200
        assert "error" in response

    def test_submit_title_only(self):
        """
        Verify you can't submit a bug with title only 
        """
        title = "app is crashing after pressing submit."
        driver = self.driver
        new_bug = NewBugPage(driver)
        new_bug.fill_title_only(title)
        response = new_bug.submit_new_bug()
        # verify you don't receive a 200 request status code
        assert response.status_code != 200
        assert "error" in response

    def test_submit_description_only(self):
        """
        Verify you can't submit a bug with description only 
        """
        description = "without filling in any text entries pressing submit crashes the app."
        driver = self.driver
        new_bug = NewBugPage(driver)
        new_bug.fill_description_only(title)
        response = new_bug.submit_new_bug()
        # verify you don't receive a 200 request status code
        assert response.status_code != 200
        assert "error" in response
    
    def submit_empty_form(self):
        """
        Verify you can't submit a bug with an empty form
        """
        title = ""
        description = ""
        driver = self.driver
        new_bug = NewBugPage(driver)
        new_bug.fill_form(title, description)
        response = new_bug.submit_new_bug()
        # verify you don't receive a 200 request status code
        assert response.status_code != 200
        assert "error" in response

    def cancel_submission(self):
        """
        Verify you can cancel a submission with the Cancel button.
        """
        title = "app is crashing after pressing submit."
        description = "without filling in any text entries pressing submit crashes the app."
        driver = self.driver
        new_bug = NewBugPage(driver)
        new_bug.fill_form(title, description)
        response = new_bug.cancel_bug_submission
        # verify you don't receive a 200 request status code
        assert response.status_code != 200
        # I'm making assumptions here because there's no info regarding
        # the state of the page after you fill out the form and click Cancel. 
        # I'm assuming it empties out the form 
        assert "title" Not in response
        assert "description" Not in response
        assert "bug id" Not in response