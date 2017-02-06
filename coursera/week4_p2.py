import urllib
from BeautifulSoup import *

#url = raw_input('Enter - ')
url = "http://python-data.dr-chuck.net/known_by_Mahmoud.html"
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
#tags = soup('span')
tags = soup('a')
#print tags
numbers = []

for i in range(1,8):
    URL_toFollow = tags[17].get('href', None)
    print tags[17].contents[0]
    html = urllib.urlopen(URL_toFollow).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    


