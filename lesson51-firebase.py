import urllib2
import requests
import json

firebaseURL = "https://fiery-torch-9187.firebaseio.com/users"

def get():
    request = urllib2.Request(firebaseURL+".json")
    response = urllib2.urlopen(request)

    print response.read()

def post(username):
    #Well, i can't get the write to work. Oh well, i'm not gonna use firebase anyway#
    data = json.dumps({"name":username})
    print requests.post(firebaseURL,data=data)