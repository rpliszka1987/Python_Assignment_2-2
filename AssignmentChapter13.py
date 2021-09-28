import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
import ssl

# This code is for SSL certificate
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')
html = urllib.request.urlopen(url, context=ctx).read()

# This code converts into an object Element Tree
stuff = ET.fromstring(html)

# Creates a list of all tags in comment
lst = stuff.findall('comments/comment')

# Print items in the lst
print('Count: ', len(lst))

total_int = 0

# Loops through the lst list
for item in lst:
    total = item.find('count').text
    total_int += int(total)

# Prints out the total
print('Sum: ', total_int)
