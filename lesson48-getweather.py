import urllib2
import json
from pprint import pprint

def getWeather(city, countryCOde):
    city = city.replace(" ", "%20")
    api = "http://api.openweathermap.org/data/2.5/weather?q={0},{1}&appid=2de143494c0b295cca9337e1e96b00e0&units=imperial".format(city, countryCOde)
    response = urllib2.urlopen(api)
    data = json.loads(response.read())
    return data


weather = getWeather("San Juan", "PR")
print "{0} degrees F".format(weather["main"]["temp"])

