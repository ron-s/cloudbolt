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





# @pytest.fixture
# def example_bug_data():
#     return
#     {
#         "bug_id": 1234,
#         "title": "The service is broken",
#         "description": "I tried this thing and it broke",
#         "status": "OPEN",
#     }


def test_add_bug():
    """
    Add a bug using title and description
    """

    bug = {
    "title": "API 404 error",
    "description": "webpage error",
    }
    title = bug['title']
    description = bug['description']
    BugTrackerService.add_bug(title, description)
    

def test_add_empty_bug():
    """
    verify submitting an empty title and description returns error or empty dictionary
    """

    expected = {
    "title": "",
    "description": "",
    }
    title = bug['title']
    description = bug['description']
    result = BugTrackerService.add_bug(title, description)
    assert expected == result
    if len(result) == 0:
        print(Dictionary is empty)
        raise error



def test_view_bug():
    """
    Lookup bug 1234 and verify the response is the same as the sample collection
    """

    expected = {
    "bug_id": 1234 ,
    "title": "The service is broken",
    "description": "I tried this thing and it broke",
    "status": "OPEN",
    }

    result = BugTrackerService.view_bug(1234)
    assert result == expected


def test_find_bug_by_name():
    """
    Verify performing a lookup by title returns based on its name
    """

def test_edit_bug_description():
    """
    verify if you can edit a bug description that it retains its state
    """