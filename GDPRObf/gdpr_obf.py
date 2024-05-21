### Main function takes JSON string with two keys
# file_to_obfuscate - one value, S3 Bucket Location of the file
# pii_fields - any amount of values, contains list of strings, each relating to a field name
# return value will be a tuple
# pass the s3 location to a function to copy the data, and convert to a pandas dataframe to make it easier to use in other functions
# take the copied data dataframe, obfuscate it, and convert it back to csv
# return a bytestream of the obfuscated csv

# final return from main should be a bytestream representation of the input file - same format

# invocation, connection to AWS/S3 etc is already handled

from parse_json import parse_json
from copy_from_s3 import copy_from_s3
from obfuscate_fields import obfuscate_fields

def gdpr_obf(json_string):
    s3_location, pii_fields = parse_json(json_string)
    copied_file = copy_from_s3(s3_location)
    obfuscated_file = obfuscate_fields(copied_file, pii_fields)
    pass 