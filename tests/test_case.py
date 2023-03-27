import requests
import pytest
import os

class Test_Create_Case():
    def test_create_case(self):
        url = 'http://dev.catlabs.zpoken.io:6020/api/v1/cases'

        data = {
            "name": "Test 111", "number": "021", "comment": "Test comment"
        }

        headers = {
            "Content-Type": "application/json"
        }

        r = requests.post(url=url, json=data, headers=headers)
        assert r.status_code == 201
        # Get Case ID for Exhibit
        data = r.json()
        value = data['data']['id']
        global CASE_ID
        CASE_ID = value