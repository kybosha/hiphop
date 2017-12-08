import requests
import datetime

#now = datetime.datetime.now()

def message_write():
    headers = {'Content-Type': 'application/json',}
    params = (('auth_token', 'hYMOQTmiYuEKZ0JnwXlYCkFdys1iAuks0gzB6C4S'),)
    data = '{"color":"green","message":"My first notification (yey)","notify":false,"message_format":"text"}'
    requests.post('https://atlassian.hipchat.com/v2/room/1622654/notification', headers=headers, params=params, data=data)
