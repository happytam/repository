import json
from urllib2 import urlopen

def getCounty(ipAddress):
    response = urlopen("http://freegeoip.net/json/"+ipAddress).read().decode('utf-8')
    responseJson = json.loads(response)
    return responseJson.get("country_code")

print(getCounty("50.78.253.58"))

