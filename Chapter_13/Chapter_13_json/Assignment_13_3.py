# The program will prompt for a location, contact a web service and retrieve JSON for the web service
# and parse that data, and retrieve the first place_id from the JSON


import urllib
import json

serviceurl = "http://python-data.dr-chuck.net/geojson?"

while True:
    location = raw_input("Enter location: \n")
    if len(location)<1: break

    url = serviceurl + urllib.urlencode({"sensor":"false","address":location})
    print "Retrieving", url

    data = urllib.urlopen(url).read()
    print "Retrieving", len(data), "characters"

    try:
        js = json.loads(data)
    except:
        js = None
    if "status" not in js or js["status"] != "OK":
        print "------- Failure To Retrieve -------"
        print data
        continue

    # print json.dumps(js, indent=4)

    print "Place id", js["results"][0]["place_id"]
