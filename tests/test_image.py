import requests
import pytest
import os
import time
from activities.create_exhibit import CreateExhibit
from activities.create_case import CreateCase

BASE_URL = 'https://dev.catlabs.zpoken.io/api/v1'
CASE_ID = ''
EXHIBIT_ID = ''
ARTIFACT_ID = ''

NUMBER = ['101', '102', '103']

COMMENT = 'TEST COMMENT'


FILE = ["../tests/files/Full_seed_eth.png",
        "../tests/files/QR_5",
        "../tests/files/seed_part_eth.png"]

class Test_create_image_case():
    def test_image_case_full_seed_phrase_eth(self):
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

    def test_image_case_part_seed_phrase_eth(self):
        # Create Exhibit
        create_exhibit = CreateExhibit()
        create_exhibit.create_exhibit_one(FILE[2])

        # Create case
        create_case = CreateExhibit()
        create_case.create_case_one("Image_Case_part_seed_ETH")

        # Get Artifact ID
        get_artifact_id = CreateExhibit()
        get_artifact_id.get_artifact_id()

        # Parse Seed
        parse_seed = CreateExhibit()
        parse_seed.parse_seed_one(50)

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

    def test_image_case_qr_wallet_address_eth(self):
        # Create Exhibit
        create_exhibit = CreateExhibit()
        create_exhibit.create_exhibit_one(FILE[1])

        # Create case
        create_case = CreateExhibit()
        create_case.create_case_one("image_case_qr_wallet_address_eth")

        # Get Artifact ID
        get_artifact_id = CreateExhibit()
        get_artifact_id.get_artifact_id()

        # Parse Seed
        parse_seed = CreateExhibit()
        parse_seed.parse_seed_one(15)

        # Check Result
        check_result = CreateExhibit()
        check_result.check_parsing_result_wallet_address()
        address, amount, chain, balance = check_result.check_parsing_result_wallet_address()
        assert address == '0x1c805E92F3542794d701fA7134Afe34b08a895c2'
        assert amount == '0.000000000000032000'
        assert chain == 'ETH'
        assert balance == 5.277376000000001e-11



