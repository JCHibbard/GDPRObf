import pytest
import json
from src.GDPRObf.parse_json import parse_json

@pytest.fixture
def input_json():
    return json.dumps({"file_to_obfuscate" : "s3://gdpr_test_bucket/test_file.csv", "pii_fields": ["name", "email"]})

def test_returns_two_outputs(input_json):
    result = len(parse_json(input_json))
    expected = 2
    assert result == expected

def test_returns_tuple_output(input_json):
    result = parse_json(input_json)
    assert isinstance(result, tuple)

def test_first_tuple_item_is_s3_location(input_json):
    result, result_2 = parse_json(input_json)
    expected = "s3://gdpr_test_bucket/test_file.csv"
    assert result == expected

def test_second_tuple_item_is_list(input_json):
    result, result_2 = parse_json(input_json)
    assert isinstance(result_2, list)
