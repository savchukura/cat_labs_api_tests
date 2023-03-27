import requests
import pytest
import os
import time

CASE_ID = ''
EXHIBIT_ID = ''
ARTIFACT_ID = ''


class CreateExhibit():

    def create_exhibit_one(self, file):
        url = 'https://dev.catlabs.zpoken.io/api/v1/exhibits'
        data = {
            "data": '{"number": "101", "comment": "Test Comment"}'
        }
        headers = {"Accept": "multipart/form-data", "Content-Length": str(os.path.abspath(file))}
        zi = open(file, 'rb')
        r = requests.post(url=url, headers=headers, data=data, files={'request_file': zi})
        zi.close()
        assert r.status_code == 201
        # Get Exhibit ID
        data = r.json()
        value = data['data']['id']
        global EXHIBIT_ID
        EXHIBIT_ID = value

    def create_case_one(self, case_name):
        url = 'https://dev.catlabs.zpoken.io/api/v1/cases'
        data = {
            "name": case_name, "number": "101", "comment": "Test comment", "exhibit_ids": [EXHIBIT_ID],
            "witness_emails": ["chronicletest@ukr.net"], 'action': 'start_full_scan'
        }
        headers = {
            "Content-Type": "application/json"
        }
        r = requests.post(url=url, json=data, headers=headers)
        print(r.status_code)
        print(r.text)
        assert r.status_code == 201
        # Get Case ID for Exhibit
        data = r.json()
        value = data['data']['id']
        global CASE_ID
        CASE_ID = value
        time.sleep(20)

    def get_artifact_id(self):
        url = 'https://dev.catlabs.zpoken.io/api/v1/exhibits/' + EXHIBIT_ID + '/artifacts'
        r = requests.get(url=url)
        print(r.text)
        assert r.status_code == 200
        # Get Artifact ID
        data = r.json()
        assert len(data["data"]) > 0
        value = data['data'][0]['id']
        global ARTIFACT_ID
        ARTIFACT_ID = value

    def parse_seed_one(self, parse_time):
        url = 'https://dev.catlabs.zpoken.io/api/v1/exhibits/' + EXHIBIT_ID + '/artifacts/' + ARTIFACT_ID
        r = requests.post(url=url)
        assert r.status_code == 200
        time.sleep(parse_time)

    def check_parsing_result(self):
        url = 'https://dev.catlabs.zpoken.io/api/v1/exhibits/' + EXHIBIT_ID + '/artifacts/' + ARTIFACT_ID
        r = requests.get(url=url)
        assert r.status_code == 200
        data = r.json()
        address = data['address']
        amount = data['assets'][0]['amount']
        chain = data['assets'][0]['chain']
        balance = data['balance']
        private_key = data['private_key']
        public_key = data['public_key']
        seed_phrase = data['subject']
        return address, amount, chain, balance, private_key, public_key, seed_phrase

    def check_parsing_result_wallet_address(self):
        url = 'https://dev.catlabs.zpoken.io/api/v1/exhibits/' + EXHIBIT_ID + '/artifacts/' + ARTIFACT_ID
        r = requests.get(url=url)
        assert r.status_code == 200
        print(r.text)
        data = r.json()
        address = data['address']
        amount = data['assets'][0]['amount']
        chain = data['assets'][0]['chain']
        balance = data['balance']
        return address, amount, chain, balance

