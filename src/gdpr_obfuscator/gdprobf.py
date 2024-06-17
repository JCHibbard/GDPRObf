"""This module is a tool used to help remove personally identifiable information from data held within an AWS S3 Bucket.
"""

import pandas as pd
import json
import boto3
import re


def gdpr_obf(input_json):
    """Handles execution of other functions in module

    Args:
        input_json (.json file, or file-like object): Contains a json file with two keys, one for the aws S3 location, and one containing a list of the names of the fields to obfuscate.

    Returns:
        Bytes: A Bytes object representing the now obfuscated data.
    """
    s3_location, pii_fields = parse_json(input_json)
    copied_df = copy_from_s3(s3_location)
    obfuscated_df = obfuscate_fields(copied_df, pii_fields)
    obfuscated_bytes = convert_to_bytes(obfuscated_df)
    return obfuscated_bytes


def parse_json(input_json):
    """Takes a json input file, and splits it into a proper S3 location, and the fields to obfuscate.

    Args:
        input_json (.json file, or file-like object): Contains a json file with two keys, one for the aws S3 location, and one containing a list of the names of the fields to obfuscate.

    Raises:
        IndexError: Error for if the user provides a .json file with too many keys.

    Returns:
        Tuple: A tuple of the S3 location and the list of fields to obfuscate.
    """
    json_dict = json.loads(input_json)
    if len(json_dict) != 2:
        raise IndexError("Input JSON is wrong length.")
    s3_location = list(json_dict.values())[0]
    pii_fields = list(json_dict.values())[1]
    return s3_location, pii_fields


def copy_from_s3(s3_location):
    """Finds the file to obfuscate within the given S3 bucket, and converts it to a pandas dataframe.

    Args:
        s3_location (String): The S3 location of the file to obfuscate.

    Returns:
        DataFrame: A pandas DataFrame representation of the file to obfuscate.
    """
    s3 = boto3.client("s3")
    regex = "(?<=s3://)([a-zA-Z-_]+)[/](.+)"
    bucket_name = re.search(regex, s3_location).group(1)
    key_name = re.search(regex, s3_location).group(2)
    s3_data = s3.get_object(Bucket=bucket_name, Key=key_name)
    copied_df = pd.read_csv(s3_data["Body"])
    return copied_df


def obfuscate_fields(copied_df, pii_fields):
    """Replaces the fields to obfuscate within the copied DataFrame with '*****'.

    Args:
        copied_df (DataFrame): A pandas DataFrame representation of the file to obfuscate.
        pii_fields (List): A list of strings containing the names of the fields to obfuscate.

    Returns:
        DataFrame: A copy of the input DataFrame, with the requested fields blanked out.
    """
    obfuscated_df = copied_df
    obfuscated_df[pii_fields] = "*****"
    return obfuscated_df


def convert_to_bytes(obfuscated_df):
    """Converts the obfuscated dataframe into Bytes.

    Args:
        obfuscated_df (DataFrame): A copy of the input DataFrame, with the requested fields blanked out.

    Returns:
        Bytes: A Bytes object representing the now obfuscated data.
    """
    obfuscated_file = obfuscated_df.to_csv(index=False)
    obfuscated_bytes = bytes(obfuscated_file, "utf-8")
    return obfuscated_bytes
