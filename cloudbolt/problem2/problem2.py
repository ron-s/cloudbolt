import pytest
import requests


url =  https://bugs.info:4000/api/v1/bug



def test_edit_bug():
    """ 
    Verify that a bug can be edited and the data persists
    """

    existing_bug = {
        "bug_id": 1234 ,
        "title": "The service is hanging",
        "description": "service hangs after casting a string",
        "status": "OPEN",
    }

    edit_bug_data = {
        "bug_id": 1234 ,
        "title": "The service starts and stops",
        "description": "Service keeps restarting and logging everyone off",
    }

    expected = {
        "bug_id": 1234 ,
        "title": "The service starts and stops",
        "description": "Service keeps restarting and logging everyone off",
        "status": "OPEN",
    }

    r = requests.post(url, edit_bug_data)
    # verify 200 request status code
    assert r.status_code == 200
    
    # lookup the bug and verify data persists
    bug_id = update_bug_data["bug_id"]
    assert r.get(url, bug_id) == expected


def test_edit_bug():
    """ 
    Verify that editing an invalid bug id results in a "Not Found" response
    """

    bug = {
        "bug_id": -200
    }
    bug_id = bug["bug_id"]
    r = requests.post(url, bug_id)
    assert "NOT FOUND" in r.raise_for_status()


def test_invalid_payload():
    """
    Verify that the server handles invalid payloads
    """

    # omit commas to create invalid payload
    update_bug_data = {
        "bug_id": 1234 
        "title": "The service is hanging"
        "description": "service hangs after casting a string"
        "status": "OPEN"
    }
    r = requests.post(url, update_bug_data)
    data = r.json
    for value in data:
        assert value["message"] == "Invalid JSON payload"


def test_create_new_bug():
    """ 
    Create a new bug and verify sucessful 200 response
    """

    data = {
        "title": "The service is broken",
        "description": "I tried this thing and it broke",
    }

    r = requests.put(url, data)
    # verify 200 request status code
    assert r.status_code == 200


def test_create_new_bug():
    """ 
    Create a new bug and verify sucessful 200 response
    """

    data = {
        "title": "The service is broken",
        "description": "I tried this thing and it broke",
    }

    r = requests.put(url, data)
    # verify 200 request status code
    assert r.status_code == 200


def test_view_invalid_bug():
    """ 
    Verify that viewing an invalid bug id results in a "Not Found" response
    """

    bug = {
        "bug_id": 100000000000000000000
    }
    bug_id = bug["bug_id"]
    r = requests.get(url, bug_id)
    assert "NOT FOUND" in r.raise_for_status()



    