#http://developer.rottentomatoes.com/
import urllib2
import json
from pprint import pprint

def movieSearch(movieName = ""):
    movieName = movieName.replace(" ", "+")
    response = urllib2.urlopen("http://www.omdbapi.com/?t={0}&r=json&tomatoes=true".format(movieName))
    data = json.loads(response.read())

    print """
    Title: {0}
    Year: {1}
    Rating: {2}
    Running time: {3}
    Description: {4}

    {5}
    """.format(data["Title"], data["Year"], data["tomatoMeter"], data["Runtime"], data["Plot"], data["tomatoConsensus"])



while True:
    movieSearch(raw_input("Movie name? "))
    print ""
    print ""