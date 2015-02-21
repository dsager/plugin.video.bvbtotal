import urllib2, sys, os

sys.path.append(os.path.join('resources', 'lib'))

from bs4 import BeautifulSoup

BASE_URL = 'https://www.bvbtotal.de'

# url = BASE_URL + '/video/champions-league/spiel-zusammenfassung2'
# response = urllib2.urlopen(url)
# html = response.read()
html = open('resources/data/cl-sz.html')

soup = BeautifulSoup(html)

for child in soup.select('#teaser_items')[0].children:
    if str(type(child)) == "<class 'bs4.element.Tag'>":
        print child.a['title'].encode('utf-8')
        print child.img['src'].encode('utf-8')
        print child.select('span.date')[0].string.encode('utf-8')


