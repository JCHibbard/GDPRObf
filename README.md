# GDPRObf
GDPRObf is a python library designed to help remove data from a table held in an AWS S3 Bucket, scrub the data held within any given fields, and return a bytestream representation of that table.

Currently, GDPRObf only works on .csv files, so please bear this in mind.
## Installation
Please ensure you are using at least Python 12.0
See the releases tab for a built version of the project, which can be downloaded and manually installed with pip.
<details>
<summary> Windows </summary>

```console
py -m pip install ./downloads/
```
</details>

<details>
<summary> Linux </summary>

```console
python3 -m pip install ./downloads/
```
</details>


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
from gdpr_obfuscator import gdprobf
# returns the newly obfuscated file as bytes
gdprobf.gdpr_obf(input_string)
```
The bytes returned from the function are the same format as the input.

## Testing
The project has been tested with Flake8 for PEP8, Bandit for Security, and Pytest for Unit Testing.
Tests must be run from the ./tests/ directory to avoid errors incorrectly showing. Deprecation warnings in tests are due to boto3.
