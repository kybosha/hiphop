import requests
import datetime

#now = datetime.datetime.now()
headers = {'Content-Type': 'application/json',}
data = '{"color":"green","message":"I love exquisite meat (notsureif)","notify":false,"message_format":"text"}'

def message_write():
    """
    requests.post('https://atlassian.hipchat.com/v2/room/1622654/notification', headers=headers, params=params, data=data)"""
    requests.post('https://atlassian.hipchat.com/v2/room/1622654/notification?auth_token=hYMOQTmiYuEKZ0JnwXlYCkFdys1iAuks0gzB6C4S', headers=headers, data=data)
    return 'ok'
