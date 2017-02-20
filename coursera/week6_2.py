import urllib
import json

APIurl = "http://python-data.dr-chuck.net/geojson?"

while True:
    address = raw_input("Enter Location: ")
    if len(address) < 1 : break
    
    url = APIurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved', len(data),'characters'
    
    js = json.loads(str(data))
    
    #print json.dumps(js, indent=4)
    
    print "Place id ", js["results"][0]["place_id"]
    