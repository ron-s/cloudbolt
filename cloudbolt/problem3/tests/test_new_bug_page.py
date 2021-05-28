from pages.bug_page import NewBugPage
from base.base import Base
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