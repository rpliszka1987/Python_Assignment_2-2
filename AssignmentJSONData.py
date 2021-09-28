import urllib.request
import urllib.parse
import urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter url: ")
connection = urllib.request.urlopen(url)
data = connection.read().decode()

print(len(data))
js = json.loads(data)

total = 0

for comment in js['comments']:
    value = comment['count']
    int_value = int(value)
    total += int_value

print('Sum:', total)
