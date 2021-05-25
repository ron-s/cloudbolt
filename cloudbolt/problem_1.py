import pytest


class BugTrackerService():
    def add_bug (title: str, description: str):
        """ returns the bug_id """
    def view_bug (bug_id: int): 
        """ returns the bug dictionary """
    def find_bug_by_name (title: str):
     """ returns the bug_id based on the name """
    def edit_bug_description (bug_id: int, description: str): 
        """ updates the bug's description """
    def edit_bug_status (bug_id: int, status: str): 
        """ sets the status field on a bug """
    def delete_bug (bug_id: int):
        """ removes the bug from the system """




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
    assert result['bug_id'] != 1234
    

def test_add_empty_bug():
    """
    Verify submitting an empty title and description returns error or empty dictionary
    """

    bug = {
    "title": "",
    "description": "",
    }
    title = bug['title']
    description = bug['description']
    result = BugTrackerService.add_bug(title, description)
    if len(result) == 0:
        print('No bug_id returned')
        assert error


def test_add_bug_empty_title():
    """
    Verify submitting an empty title returns error or empty dictionary
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
    Verify submitting an empty title returns error or empty dictionary
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
    Verify submitting an integer as title and dictionary returns an error
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

    expected = {}
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
    Verify if you can edit a bug description and that it updates the description entirely and does not append added desc.
    """

    expected = {
    "bug_id": 2345 ,
    "title": "The service is hanging",
    "description": "service hangs after casting a string using AWS",
    "status": "OPEN",
    }

    BugTrackerService.edit_bug_description(2345, 'service hangs after casting a string using AWS')
    result = BugTrackerService.view_bug(2345)
    assert expected == result


def test_edit_bug_status():
    """
    Verify if you can edit the bug's status from OPEN to CLOSED.
    """

    expected = {
    "bug_id": 1234 ,
    "title": "The service is broken",
    "description": "I tried this thing and it broke",
    "status": "CLOSED",
    }
    BugTrackerService.edit_bug_status(1234, 'CLOSED')
    result == BugTrackerService.view_bug(1234)
    assert expected == result


def test_delete_bug():
    """
    Verify you can delete a bug by bug_id, but make sure the bug exists first
    """

    # add new bug and verify it exists 
    add_new_bug = {
    "title": "React page won't load",
    "description": "Using this URL webpage won't load"
    }
    title = add_new_bug['title']
    description = add_new_bug = ['description']
    new_bug = BugTrackerService.add_bug(title, description)
    bug_id = new_bug['bug_id']

    # delete the new bug
    BugTrackerService.delete_bug(bug_id)
    if len(BugTrackerService.view_bug(bug_id)) == 0:
        print('Bug deleted')
    else:
        assert error



