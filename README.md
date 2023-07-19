# ASN-Lookup
This script allows you to lookup ASNs and get the associated IP ranges.

## Usage
To use the script, you will need to install the requests Python package. You can do this by running the following command:
- pip install requests
- pip install tqdm

Once you have installed the package, you can run the script by typing the following command into the command line:
- python asn_lookup.py

The script will prompt you to enter one or more ASN numbers. You can enter up to 20 ASN numbers. Once you have entered the ASN numbers, the script will generate a file named ip_ranges.lst that contains the subnets associated with the ASN numbers that you entered.

## Example
Here is an example of how to use the script:
- python asn_lookup.py 1234,5678,9012
- python asn_lookup.py

This will run the script and generate a file named ip_ranges.lst that contains the subnets associated with the ASN numbers 1234, 5678, and 9012.

## Requirements
Python 3.6+

requests Python package

## Author
This script was created by Zyrik.
