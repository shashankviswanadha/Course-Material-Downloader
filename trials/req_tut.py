import requests
from bs4 import BeautifulSoup
data = requests.get('http://hyderabad.yellowpages.co.in/Restaurant')
r = data.content
soup = BeautifulSoup(r)
#print soup.find_all("a")
#print soup.prettify
for link in soup.find_all("a"):
    #print link.text,link.get('href')
    if link.get('href') != None:
        if 'http' in link.get('href'):
            print "<a href='%s'>%s</a>" %(link.get('href'),link.text)

g_data = soup.find_all("div",{"class":"info"})
print g_data
