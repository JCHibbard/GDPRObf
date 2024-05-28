import pytest
import pandas as pd
import moto

from src.GDPRObf.gdpr_obf import gdpr_obf, copy_from_s3, convert_to_bytes, obfuscate_fields, parse_json

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

class TestCopyFromS3:
    def test_returns_dataframe(self, aws, create_bucket, add_files_to_bucket):
        result = copy_from_s3("s3://gdpr-test-bucket/mock_data.csv")
        assert isinstance(result, pd.DataFrame)

class TestParseJSON:
    def test_returns_two_outputs(self, input_json):
        result = len(parse_json(input_json))
        expected = 2
        assert result == expected

    def test_returns_tuple_output(self, input_json):
        result = parse_json(input_json)
        assert isinstance(result, tuple)

    def test_first_tuple_item_is_s3_location(self, input_json):
        result, result_2 = parse_json(input_json)
        expected = "s3://gdpr_test_bucket/test_file.csv"
        assert result == expected

    def test_second_tuple_item_is_list(self, input_json):
        result, result_2 = parse_json(input_json)
        assert isinstance(result_2, list)
