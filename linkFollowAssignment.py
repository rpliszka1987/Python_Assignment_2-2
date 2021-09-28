import urllib.request
import urllib.parse
import urllib.error

from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')
count = input('Enter count: ')
position = input('Enter position: ')
count_int = int(count)
position_int = int(position) - 1
i = 0
print('Retriving', url)

while i < count_int:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    tags = soup('a')

    for tag in tags:
        links.append(tag.get('href', None))
    print('Retriving', links[int(position_int)])
    url = links[int(position_int)]
    i += 1
