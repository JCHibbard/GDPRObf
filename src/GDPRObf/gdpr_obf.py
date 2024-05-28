import pandas as pd
import boto3
import re
import json

def gdpr_obf(input_json):
    s3_location, pii_fields = parse_json(input_json)
    copied_df = copy_from_s3(s3_location)
    obfuscated_df = obfuscate_fields(copied_df, pii_fields)
    obfuscated_bytes = convert_to_bytes(obfuscated_df)
    return obfuscated_bytes

def copy_from_s3(s3_location):
    s3 = boto3.client('s3')
    regex = "(?<=s3://)([a-zA-Z-]+)[/](.+)"
    bucket_name = re.search(regex, s3_location).group(1)
    key_name = re.search(regex, s3_location).group(2)
    s3_data = s3.get_object(Bucket=bucket_name, Key=key_name)
    copied_df = pd.read_csv(s3_data['Body'])
    return copied_df

def convert_to_bytes(obfuscated_df):
    obfuscated_file = obfuscated_df.to_csv(index=False)
    obfuscated_bytes = bytes(obfuscated_file, 'utf-8')
    return obfuscated_bytes

def obfuscate_fields(copied_df, pii_fields):
    obfuscated_df = copied_df
    obfuscated_df[pii_fields] = '*****'
    return obfuscated_df

def parse_json(input_json):
    json_dict = json.loads(input_json)
    if len(json_dict) != 2:
        raise IndexError("Input JSON is wrong length")
    s3_location = list(json_dict.values())[0]
    pii_fields = list(json_dict.values())[1]
    return s3_location, pii_fields
