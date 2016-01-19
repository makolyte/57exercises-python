import urllib2
import json
from pprint import pprint

response = urllib2.urlopen("http://api.open-notify.org/astros.json")
data = json.loads(response.read())

print "There are {0} people in space right now".format(data["number"])

def p(name, craft, filler=' '):
    formatString = "{0}|{1}"
    print formatString.format(name.ljust(20, filler), craft.ljust(10,filler))

p("Name", "Craft")
p('','', '-')
for line in data["people"]:
    p(line["name"], line["craft"])
