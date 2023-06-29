import json
from urllib.parse import urlencode
from urllib.request import urlopen
from pathlib import Path
from pprint import pprint
api_key = open(str(Path.home()) + "/.google_api_key").read()
query = "Mark Louis Watson"
service_url = "https://kgsearch.googleapis.com/v1/entities:search"
params = {
    "query": query,
    "limit": 10,
    "indent": True,
    "key": api_key,
}
url = service_url + "?" + urlencode(params)
response = json.loads(urlopen(url).read())
pprint(response)