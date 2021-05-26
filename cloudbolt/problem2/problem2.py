import pytest
import requests


url =  https://bugs.info:4000/api/v1/bug


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




def test_edit_bug():
    """ 
    Verify that a bug can be edited
    """

    existing_bug = {
        "bug_id": 1234 ,
        "title": "The service is hanging",
        "description": "service hangs after casting a string",
        "status": "OPEN",
    }

    update_bug_data = {
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

    r = requests.post(url, update_bug_data)
    # verify 200 request status code
    assert r.status_code == 200
    
    # lookup the bug and verify data persist
    bug_id = update_bug_data['bug_id']
    assert r.get(url, bug_id) == expected


    

