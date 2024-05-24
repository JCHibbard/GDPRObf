import pytest
import pandas as pd
from src.GDPRObf.obfuscate_fields import obfuscate_fields, convert_to_bytes

class TestObfuscateFields:
    def test_returns_a_pandas_dataframe(self, test_dataframe):
        result = obfuscate_fields(test_dataframe, ['name', 'phone'])
        assert isinstance(result, pd.DataFrame)

    def test_returns_obfuscated_dataframe(self, test_dataframe, test_obfurscated_dataframe):
        expected = test_obfurscated_dataframe
        result = obfuscate_fields(test_dataframe, ['name', 'phone'])
        pd.testing.assert_frame_equal(expected, result)

class TestConvertToBytes:
    def test_returns_bytes_object(self, test_obfurscated_dataframe):
        result = convert_to_bytes(test_obfurscated_dataframe)
        assert isinstance(result, bytes)