import urllib
import json

while True:
    url = raw_input("Enter URL: ")
    uh = urllib.urlopen(url)
    
    print "Retrieving", url
    data = uh.read()
    print 'Retrieved', len(data),'characters'
    
    try:
        js = json.loads(str(data))
    except:
        js = None
        print '==== Something Failed ===='
        continue
    
    print json.dumps(js, indent=4)
    sum = 0
    for comment in js["comments"]:
        sum += comment["count"]
        
    print "Result -->", sum