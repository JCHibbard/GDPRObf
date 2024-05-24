import pytest
import pandas as pd
from src.GDPRObf.obfuscate_fields import obfuscate_fields

def test_returns_a_pandas_dataframe(test_dataframe):
    result = obfuscate_fields(test_dataframe, ['name', 'phone'])
    assert isinstance(result, pd.DataFrame)

def test_returns_obfuscated_dataframe(test_dataframe, test_obfurscated_dataframe):
    expected = test_obfurscated_dataframe
    result = obfuscate_fields(test_dataframe, ['name', 'phone'])
    pd.testing.assert_frame_equal(expected, result)
    assert False
        