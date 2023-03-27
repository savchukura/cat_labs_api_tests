import requests
import pytest
import os
import time

CASE_ID = ''
EXHIBIT_ID = ''
ARTIFACT_ID = ''


class CreateCase():

    def create_case_one(self):

        url = 'https://dev.catlabs.zpoken.io/api/v1/cases'
        data = {
            "name": "Test 111", "number": "101", "comment": "Test comment", "exhibit_ids": [EXHIBIT_ID],
            "witness_emails": ["chronicletest@ukr.net"], 'action': 'start_full_scan'
        }
        headers = {
            "Content-Type": "application/json"
        }
        r = requests.post(url=url, json=data, headers=headers)
        print(r.text)
        assert r.status_code == 201
        # Get Case ID for Exhibit
        data = r.json()
        value = data['data']['id']
        global CASE_ID
        CASE_ID = value
        time.sleep(15)
