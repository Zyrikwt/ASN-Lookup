import requests
import json
import sys

def get_asn_info(asn_number):
  """Gets ASN information from the BGPView API."""
  url = f'https://api.bgpview.io/asn/{asn_number}/prefixes'
  response = requests.get(url)
  data = response.json()
  return data

def get_subnets(asn_info):
  """Gets the subnets associated with an ASN."""
  subnets = []
  for prefix in asn_info['data']['ipv4_prefixes']:
    subnets.append(prefix['prefix'])
  return subnets

def write_subnets_to_file(subnets, file_name):
  """Writes the subnets to a LST file."""
  with open(file_name, 'w') as f:
    for subnet in subnets:
      f.write(subnet + '\n')

def main():
  """Main function."""
  asn_numbers = []
  max_asns = 20
  print('** ASN to IP Range**')
  print(f'Recommended: >{max_asns} ASNs.')
  asn_numbers = input('Enter ASN(s): ').split(',')
  print('** Generating **')
  subnets = []
  for asn_number in asn_numbers:
    asn_info = get_asn_info(asn_number)
    subnets.extend(get_subnets(asn_info))
  file_name = 'ip_ranges.lst'
  write_subnets_to_file(subnets, file_name)

  # Add completed text
  print('** Completed **')
  print(f'The file "ip_ranges.lst" has been generated.')

if __name__ == '__main__':
  main()
