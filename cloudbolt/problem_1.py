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
    # verify title isn't missing
    if self.bug['title'] == None:
        print("Missing title")
    # verify description isn't missing
    elif self.bug['description'] == None:
        print("Missing description")
    else:
        assert self.BugTrackerService.add_bug(title, description) != bug[1234]


    def test_view_bug(self):
    """
    view bug info as dictionary
    """

    bug_id = bug[1234]
    # lookup bug 1234 and verify it contains the same info as the orignal collection
    self.BugTrackerService.view_bug(bug_id)
    assert self.bug['title'] is not None 
    assert self.bug['title'] == 'The service is broken'
    assert self.bug['description'] is not None
    assert self.bug['description'] == 'I tried this thing and it broke'
    assert self.bug['status'] is not None
    assert self.bug['status'] == 'OPEN'

