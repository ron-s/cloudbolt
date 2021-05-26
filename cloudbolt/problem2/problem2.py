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
    assert response.status_code == 200
    



