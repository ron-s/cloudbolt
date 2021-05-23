import pytest


class BugTrackerService():
    def add_bug (title: str, description: str) -> int:
        """ returns the bug_id """
    def view_bug (bug_id: int) -> dict: 
        """ returns the bug dictionary """
    def find_bug_by_name (title: str) -> int:
        """ returns the bug_id based on the name """
    def edit_bug_description (bug_id: int, description: str) -> None : 
        """ updates the bug's description """
    def edit_bug_status (bug_id: int, status: str) -> None : 
        """ sets the status field on a bug """
    def delete_bug (bug_id: int) -> None : 
        """ removes the bug from the system """


class CloudboltTests():

    bug = {
    "bug_id": 1234 ,
    "title": "The service is broken",
    "description": "I tried this thing and it broke",
    "status": "OPEN",
    }

    def test_add_bug(self)
    """
    Add a bug, verify the title and desc aren't empty and verify the bug ID is unique
    """

    title = bug['title']
    description = bug ['description']
    if self.bug['title'] == None:
        print("Missing title")
    elif self.bug['description'] == None:
        print("Missing description")
    else:
        assert self.BugTrackerService.add_bug(title, description) != bug[1234]


    def test_view_bug(self):
    """
    view bug dictionary
    """

    bug_id = bug[1234]
    self.BugTrackerService.view_bug(bug_id)
    assert  self.BugTrackerService.view_bug

