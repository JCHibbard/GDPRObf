# GDPRObf
GDPRObf is a python library designed to help remove data from a table held in an AWS S3 Bucket, scrub the data held within any given fields, and return a bytestream representation of that table.

Currently, GDPRObf only works on .csv files, so please bear this in mind.
## Installation

## Usage
GDPRObf takes a .json input with two keys; a string for the S3 location requested, and a list of the names of the fields to obfuscate, as shown below:
```json
{
    "S3 location of file": "s3://example-location/example-file.csv",
    "Names of field(s) to obfuscate": ["name", "email"]
}
```
The function should be used as such:
```python
# returns the newly obfuscated file as bytes
gdpr_obf(input_string)
```
The bytes returned from the function are the same format as the input.