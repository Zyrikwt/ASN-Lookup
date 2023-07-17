ASN to IPRange tool.

The more ASNs you enter, the longer it takes to generate. 
I limited to 20 because the BGPView API has a limit of 20 requests per minute.
Enter any more than 20, and the script will hang.

Make sure to download all requirements.
Make sure to CD into the file.

-- USAGE: --
Run:
pip install requests

Examples of Use:
python asn.py
python asn.py as1,as2,as3,
