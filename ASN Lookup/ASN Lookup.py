import requests
import json
import sys
import time
import random
import tqdm

def get_asn_info(asn_number):
  """Gets ASN information from the BGPView API."""
  url = f'https://api.bgpview.io/asn/{asn_number}/prefixes'
  try:
    response = requests.get(url)
    data = response.json()
    return data
  except requests.exceptions.RequestException as e:
    raise ValueError(f'API returned an error: {e}')

def get_subnets(asn_info):
  """Gets the subnets associated with an ASN."""
  subnets = [
      prefix['prefix']
      for prefix in asn_info['data']['ipv4_prefixes']
  ]
  return subnets

def write_subnets_to_file(subnets, file_name='ip_ranges.lst'):
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
  try:
    asn_numbers = input('Enter ASN(s): ').split(',')
  except ValueError as e:
    print(e)
    sys.exit()
  print('** Generating **')
  subnets = []
  with tqdm.tqdm(total=len(asn_numbers), ncols=60) as pbar:
    for asn_number in asn_numbers:
      if len(asn_numbers) > max_asns:
        print(f'Error: The maximum number of ASNs is {max_asns}.')
        sys.exit()
      try:
        pbar.update(1)
        asn_info = get_asn_info(asn_number)
      except ValueError as e:
        print(e)
        continue
      subnets.extend(get_subnets(asn_info))
  file_name = 'ip_ranges.lst'
  write_subnets_to_file(subnets)

  print('** Completed **')
  print(f'The file "{file_name}" has been generated.')

if __name__ == '__main__':
  main()
