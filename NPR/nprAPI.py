
from urllib2 import urlopen
from json import load

key = 'MDE5MjQwNDkzMDE0MzIyMzIxNTk1ZjZiYQ001'
url = "http://api.npr.org/transcript?apiKey="
url += key
url += "&format=json"
url += "&id=152248901"

response = urlopen(url)
j = load(response)

for paragraph in j['paragraph']:
    print paragraph["$text"] + "\n"
