"""Pridava a odobera hviezdicky na githube

Usage: hviezdicka.py (add | remove) --token=TOKEN <username> <reponame>

"""

import requests
import pprint
import sys
import docopt

options=docopt.docopt(__doc__)
token = options["--token"]

headers = {'Authorization': 'token {}'.format(token)}
username = options["<username>"]
reponame = options["<reponame>"]
url = 'https://api.github.com/user/starred/{}/{}'.format(username, reponame)
if options["add"]:
    r = requests.put(url, headers=headers)
else:
    r = requests.delete(url, headers=headers)
