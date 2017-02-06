import urllib
from BeautifulSoup import *

#url = raw_input('Enter - ')
url = "http://python-data.dr-chuck.net/comments_353155.html"
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('span')
numbers = []
for tag in tags:
    # Look at the parts of a tag
    #print 'TAG:',tag
    #print 'URL:',tag.get('href', None)
    #print 'Contents:',tag.contents[0]
    numbers.append(int(tag.contents[0]))

print "Count: ", len(numbers)
print "SUM: ", sum(numbers)
