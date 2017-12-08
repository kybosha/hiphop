import requests
import datetime

now = datetime.datetime.now()
url = "https://atlassian.hipchat.com/v2/room/1622654/notification?auth_token=hYMOQTmiYuEKZ0JnwXlYCkFdys1iAuks0gzB6C4S"

def message_write():
    r = requests.post(url, headers={"color":"green","message":str(now) + " (yey)","notify":false,"message_format":"text"})
    print(r.status_code)
