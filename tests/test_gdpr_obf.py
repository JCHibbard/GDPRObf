import pandas as pd
import pytest
from gdprobf import (
    obfuscate_fields,
    convert_to_bytes,
    copy_from_s3,
    parse_json,
    gdpr_obf,
)


class TestObfuscateFields:
    def test_returns_a_pandas_dataframe(self, test_dataframe):
        result = obfuscate_fields(test_dataframe, ["name", "phone"])
        assert isinstance(result, pd.DataFrame)

    def test_returns_obfuscated_dataframe(
        self, test_dataframe, test_obfurscated_dataframe
    ):
        expected = test_obfurscated_dataframe
        result = obfuscate_fields(test_dataframe, ["name", "phone"])
        pd.testing.assert_frame_equal(expected, result)


class TestConvertToBytes:
    def test_returns_bytes_object(self, test_obfurscated_dataframe):
        result = convert_to_bytes(test_obfurscated_dataframe)
        assert isinstance(result, bytes)


class TestCopyFromS3:
    def test_returns_dataframe(self, aws, create_bucket, add_files_to_bucket):
        result = copy_from_s3("s3://gdpr-test-bucket/mock_data.csv")
        assert isinstance(result, pd.DataFrame)

    def test_returns_correct_dataframe(
        self, aws, create_bucket, add_files_to_bucket, test_dataframe
    ):
        result = copy_from_s3("s3://gdpr-test-bucket/mock_data.csv")
        expected = test_dataframe
        pd.testing.assert_frame_equal(result, expected)


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
        expected = "s3://gdpr-test-bucket/mock_data.csv"
        assert result == expected

    def test_second_tuple_item_is_list(self, input_json):
        result, result_2 = parse_json(input_json)
        assert isinstance(result_2, list)

    def test_exception_handled_if_input_has_too_many_keys(self, bad_input):
        with pytest.raises(IndexError) as excinfo:
            parse_json(bad_input)
        assert excinfo.type is IndexError


class TestGdprObf:
    def test_returns_bytestream(
        self,
        input_json,
        aws,
        create_bucket,
        add_files_to_bucket,
    ):
        result = gdpr_obf(input_json)
        assert isinstance(result, bytes)

    def test_processes_large_file_under_one_minute(
        self, input_json, aws, create_bucket, add_big_files_to_bucket
    ):
        result = gdpr_obf(input_json)
