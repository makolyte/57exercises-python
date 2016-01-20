import urllib2
import json
from pprint import pprint

response = urllib2.urlopen("http://localhost:5000/time/JSON")
data = json.loads(response.read())
pprint(data)

