import pytest
import pandas as pd
from src.GDPRObf.copy_from_s3 import copy_from_s3


def test_returns_dataframe(aws, create_bucket, add_files_to_bucket):
    result = copy_from_s3("s3://gdpr-test-bucket/mock_data.csv")
    assert isinstance(result, pd.DataFrame)