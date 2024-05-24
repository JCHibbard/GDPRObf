def convert_to_bytes(obfuscated_df):
    obfuscated_file = obfuscated_df.to_csv(index=False)
    obfuscated_bytes = bytes(obfuscated_file, 'utf-8')
    return obfuscated_bytes

def obfuscate_fields(copied_df, pii_fields):
    obfuscated_df = copied_df
    obfuscated_df[pii_fields] = '*****'
    return obfuscated_df