import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

total = 0
tags = soup('span')
for tag in tags:
    value = tag.contents[0]
    total = total + int(value)

print(total)
