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
    result = BugTrackerService.add_bug(title, description)
    assert result[bug_id] != 1234
    

def test_add_empty_bug():
    """
    verify submitting an empty title and description returns error or empty dictionary
    """

    bug = {
    "title": "",
    "description": "",
    }
    title = bug['title']
    description = bug['description']
    result = BugTrackerService.add_bug(title, description)
    if len(result) == 0:
        print(No bug_id returned)
        assert error

def test_add_bug_empty_title():
    """
    verify submitting an empty title returns error or empty dictionary
    """
    bug = {
    "title": "",
    "description": "400 bad request",
    }
    title = bug['title']
    description = bug['description']
    result = BugTrackerService.add_bug(title, description)
    if len(result) == 0:
        print('No bug id returned')
        assert error

def test_add_bug_empty_description():
    """
    verify submitting an empty title returns error or empty dictionary
    """
    bug = {
    "title": "401 unauthorized",
    "description": "",
    }
    title = bug['title']
    description = bug['description']
    result = BugTrackerService.add_bug(title, description)
    if len(result) == 0:
        print('No bug id returned')
        assert error

def test_add_bug_using_integers():
    """
    verify submitting an integer as title and dictionary returns an error
    """
    bug = {
    "title": 2345,
    "description": 987687543677,
    }
    title = bug['title']
    description = bug['description']
    result = BugTrackerService.add_bug(title, description)
    if len(result) == 0:
        print('No bug id returned')
        assert error


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


def test_view_bug():
    """
    Lookup bug 1234 and verify the response is not the same as the sample collection
    """

    expected = {
    "bug_id": 2345 ,
    "title": "The service is hanging",
    "description": "service hangs after casting a string",
    "status": "OPEN",
    }

    result = BugTrackerService.view_bug(1234)
    assert result != expected

def test_view_bug_using_string():
    """
    Lookup bug using a string instead of an integer and verify you receive error
    """

    expected = error
    result = BugTrackerService.view_bug('This is a bug id')
    assert result == expected


def test_find_bug_by_name():
    """
    Verify a lookup by title returns associated bug
    """

    expected = {
    "bug_id": 2345
    }

    result = BugTrackerService.find_bug_by_name('the service is hanging')
    assert result[bug_id] == expected[bug_id]

def test_find_bug_by_name():
    """
    Verify a lookup by partial title returns associated bug
    """

    expected = {
    "bug_id": 2345 ,
    "title": "The service is hanging",
    "description": "service hangs after casting a string",
    "status": "OPEN",
    }

    result = BugTrackerService.find_bug_by_name('the service')
    for bug in result:
        assert result[title] in expected[title]


def test_find_bug_by_partial_name():
    """
    Verify a lookup by partial title returns associated bug
    """

    expected = {
    "bug_id": 2345 ,
    "title": "The service is hanging",
    "description": "service hangs after casting a string",
    "status": "OPEN",
    }

    result = BugTrackerService.find_bug_by_name('the service')
    for bug in result:
        assert result[title] in expected[title]


def test_find_bug_by_name_using_int():
    """
    Verify a lookup by title using an integer returns an error
    """

    result = BugTrackerService.find_bug_by_name(1099)
    if len(result) == 0:
        print('No bug id returned')
        assert error


def test_edit_bug_description():
    """
    verify if you can edit a bug description that it retains its state
    """