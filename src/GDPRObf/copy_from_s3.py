import pandas as pd
import boto3
import re


def copy_from_s3(s3_location):
    # Initialise boto3
    s3 = boto3.client('s3')
    # Regex string for bucket name (Modify regex to ensure that it captures FULL bucket, not just outer dir)
    regex = "(?<=s3://)([a-zA-Z-]+)[/](.+)"
    # Strip bucket name and key name from input string
    bucket_name = re.search(regex, s3_location).group(1)
    key_name = re.search(regex, s3_location).group(2)
    # Take S3 location and use s3.get_object
    s3_data = s3.get_object(Bucket=bucket_name, Key=key_name)
    # Create pandas dataframe from streaming body
    copied_df = pd.read_csv(s3_data['Body'])
    # Return dataframe
    return copied_df