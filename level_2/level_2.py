#!/usr/bin/python3
import requests

host = "http://158.69.76.135/level2.php"

for i in range(1024):
    req_get = requests.get(host)
    header = {
        "Referer": "http://158.69.76.135/level2.php",
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0WOW64 rv: 44.0) Gecko/20100101\
             Firefox/44.0",
    }
    payload = {'id': '1452', 'holdthedoor': 'submit',
               'key': req_get.cookies['HoldTheDoor']}
    cookies = {'HoldTheDoor': req_get.cookies['HoldTheDoor']}
    req_post = requests.post(host, payload, headers=header, cookies=cookies)
