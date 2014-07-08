import requests
import pprint
import sys

token = sys.argv[1]
headers = {'Authorization': 'token {}'.format(token)}
r = requests.get('https://api.github.com', headers=headers)
pprint.pprint(r.json())

