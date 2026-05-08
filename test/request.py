import argparse
import requests


parser = argparse.ArgumentParser(description='request url [--url]')
parser.add_argument("--url",default="http://localhost", help="Url for get")
args = parser.parse_args()

try:
  r = requests.get(url=args.url,verify=False, timeout=3)
  if r.status_code == 200:
    print(f"{args.url} - OK (200)")
  else :
    print(f"{args.url} - WARNING ({r.raise_for_status()})")
except requests.exceptions.InvalidSchema :
  print(f"Не введен schema (http or https)")
except requests.exceptions.HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except requests.exceptions.ConnectionError as conn_err:
    print(f'Connection error occurred: {conn_err}')
except requests.exceptions.Timeout as timeout_err:
    print(f'Timeout error occurred: {timeout_err}')
except requests.exceptions.RequestException as err:
    print(f'An error occurred: {err}')
