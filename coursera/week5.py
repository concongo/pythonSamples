import urllib
import xml.etree.ElementTree as ET


while True:
    url = raw_input('Enter location: ')
    if len(url) < 1 : break

    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    print data
    tree = ET.fromstring(data)


    results = tree.findall('comments')
    res_2 = results[0].findall('comment')
    print "Count: ", len(res_2)
    sum = 0
    for record in res_2:
        sum += int(record.find('count').text)
        
    print "Sum: ", sum
    