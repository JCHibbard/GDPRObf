import pandas as pd

def obfuscate_fields(copied_df, pii_fields):
    obfuscated_df = copied_df
    obfuscated_df[pii_fields] = '*****'
    return obfuscated_df