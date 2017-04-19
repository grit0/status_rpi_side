import requests
import json

send_url = 'http://freegeoip.net/json'
r = requests.get(send_url)
j = json.loads(r.text)
print(r,'\n')
print(j)
