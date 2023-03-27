import requests
import pytest
import os
import time
from activities.create_exhibit import CreateExhibit
from activities.create_case import CreateCase

BASE_URL = 'https://dev.catlabs.zpoken.io:6020/api/v1'
CASE_ID = ''
EXHIBIT_ID = ''
ARTIFACT_ID = ''

NUMBER = ['101', '102', '103']

COMMENT = 'TEST COMMENT'


FILE = ["../tests/files/Full_seed_eth.png",
        "files/Full_seed_eth.png",
        "../tests/files/exodus-macos-arm64-22.12.5.dmg"]
def test_api_one():

    url = 'https://catlabs.vizit-net.com'


    data = {"type":"zcash","wallets":["t1Poz4G4iwAoerGjXgCw5BqGmL9QATdPkDR"]}
    response = requests.post(url, json=data)

    assert response.status_code == 200
    print(response.json())


def test_create_image_case():
    url = 'https://dev.catlabs.zpoken.io/api/v1/exhibits'

    file_path = "C:/Users/Admin/PycharmProjects/cat_labs_api_tests/tests/files/Full_seed_eth.png"
    data = {
        "data": '{"number": "021", "comment": "Test Comment"}'
    }
    headers = {"Accept": "multipart/form-data", "Content-Length": str(os.path.abspath("files/wallet_address_eth.txt"))}
    with open(file_path, 'rb') as file:
        files = {'Full_seed_eth.png': file}  # Create a dictionary with the file object
        response = requests.post(url=url, headers=headers, data=data, files={'request_files': files})
        print(response.text)


    assert response.status_code == 200
    print(response.json())


class Test_Create_Case():
    def test_create_exhibit(self):
        url = 'https://dev.catlabs.zpoken.io/api/v1/exhibits'
        data = {
            "data": '{"number": "021", "comment": "Test Comment"}'
        }
        headers = {"Accept": "multipart/form-data", "Content-Length": str(os.path.abspath("files/Full_seed_eth.png"))}
        zi = open('files/Full_seed_eth.png', 'rb')
        r = requests.post(url=url, headers=headers, data=data, files={'request_file': zi})
        zi.close()
        print(r.text)
        assert r.status_code == 201

        # Get Exhibit ID
        data = r.json()
        value = data['data']['id']
        global EXHIBIT_ID
        EXHIBIT_ID = value

    def test_create_case(self):
        url = 'https://dev.catlabs.zpoken.io/api/v1/cases'

        data = {
            "name": "Test 111", "number": "021", "comment": "Test comment", "exhibit_ids": [EXHIBIT_ID],
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

    def test_get_selected_exhibit(self):
        url = 'https://dev.catlabs.zpoken.io/api/v1/exhibits/' + EXHIBIT_ID + '/artifacts'
        #url = 'https://dev.catlabs.zpoken.io/api/v1/exhibits/db4d5f76-b10b-4da1-93f5-a769a694c5b3/artifacts'
        r = requests.get(url=url)
        print(r.text)
        assert r.status_code == 200
        # Get Artifact ID
        data = r.json()

        assert len(data["data"]) > 0
        value = data['data'][0]['id']
        global ARTIFACT_ID
        ARTIFACT_ID = value
        print(ARTIFACT_ID)

    def test_parse_seed(self):
        url = 'https://dev.catlabs.zpoken.io/api/v1/exhibits/' + EXHIBIT_ID + '/artifacts/' + ARTIFACT_ID
        r = requests.post(url=url)
        assert r.status_code == 200
        time.sleep(15)
        print(r.text)

    def test_parse_seed_result(self):
        url = 'https://dev.catlabs.zpoken.io/api/v1/exhibits/' + EXHIBIT_ID + '/artifacts/' + ARTIFACT_ID
        r = requests.get(url=url)
        assert r.status_code == 200
        print(r.text)
        data = r.json()
        address = data['address']
        amount = data['assets'][0]['amount']
        chain = data['assets'][0]['chain']
        balance = data['balance']
        private_key = data['private_key']
        public_key = data['public_key']
        seed_phrase = data['subject']

        assert address == '0x1c805E92F3542794d701fA7134Afe34b08a895c2'
        assert amount == '0.000000000000032000'
        assert chain == 'ETH'
        assert balance == 5.277376000000001e-11
        assert private_key == 'e4d67889177aa11c4c0d5c3574166c21d72876842832c871a5fb39e23b4d2f3a'
        assert public_key == '03625a51b1447fd8b1e85a3898725a4bd08986e833501cd3f92cf8a29389f45466'
        assert seed_phrase == 'slab wise seat vague tennis section black scare father inmate ostrich follow'

class Test_drop_test():
    def test_create_image_case(self):
        # Create Exhibit
        create_exhibit = CreateExhibit()
        create_exhibit.create_exhibit_one(FILE[0])

        # Create case
        create_case = CreateExhibit()
        create_case.create_case_one("Image_Case_full_seed_ETH")

        # Get Artifact ID
        get_artifact_id = CreateExhibit()
        get_artifact_id.get_artifact_id()

        # Parse Seed
        parse_seed = CreateExhibit()
        parse_seed.parse_seed_one(15)

        # Check Result
        check_result = CreateExhibit()
        check_result.check_parsing_result()
        address, amount, chain, balance, private_key, public_key, seed_phrase = check_result.check_parsing_result()
        assert address == '0x1c805E92F3542794d701fA7134Afe34b08a895c2'
        assert amount == '0.000000000000032000'
        assert chain == 'ETH'
        assert balance == 5.277376000000001e-11
        assert private_key == 'e4d67889177aa11c4c0d5c3574166c21d72876842832c871a5fb39e23b4d2f3a'
        assert public_key == '03625a51b1447fd8b1e85a3898725a4bd08986e833501cd3f92cf8a29389f45466'
        assert seed_phrase == 'slab wise seat vague tennis section black scare father inmate ostrich follow'


