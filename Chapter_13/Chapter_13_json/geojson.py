# The program takes the search string and constructs a URL with the search string as a properly encoded parameter
# and then uses urllib to retrieve the text from the Google geocoding API. Unlike a fixed web page,
# the data we get depends on the parameters we send and the geographical data stored in Google servers.
#
# Once we retrieve the JSON data, we parse it with the json library
# and do a few checks to make sure that we received good data,
# then extract the information that we are looking for.

import urllib
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
# serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
    address = raw_input('\n Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor': 'false', 'address': address})
    print 'Retrieving', url
    data = urllib.urlopen(url).read()
    # print type(data)
    print 'Retrieved',len(data),'characters'

    try: js = json.loads(str(data))
    except: js = None


    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure To Retrieve ===='
        print data
        continue

    print json.dumps(js, indent=4)

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print 'lat',lat,'lng',lng
    location = js['results'][0]['formatted_address']
    print location
