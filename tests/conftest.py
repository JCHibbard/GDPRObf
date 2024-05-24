import pytest
import json
import pandas as pd

@pytest.fixture(scope="module")
def test_dataframe():
    return pd.read_csv('./test_data/MOCK_DATA.csv')

@pytest.fixture(scope="module")
def test_obfurscated_dataframe():
    return pd.read_csv('./test_data/MOCK_DATA_OBF.csv')

@pytest.fixture(scope="module")
def input_json():
    return json.dumps({"file_to_obfuscate" : "s3://gdpr_test_bucket/test_file.csv", "pii_fields": ["name", "email"]})
