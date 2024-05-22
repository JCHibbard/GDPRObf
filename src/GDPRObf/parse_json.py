### Takes JSON file from main
# Returns two values
# First is S3 location as a string
# Second is a list of the pii fields
import json

def parse_json(input_json):
    json_dict = json.loads(input_json)
    if len(json_dict) != 2:
        raise IndexError("Input JSON is wrong length")
    s3_location = list(json_dict.values())[0]
    pii_fields = list(json_dict.values())[1]
    return s3_location, pii_fields
