import requests
import json

def send_sms(number, message):
    url = "https://www.fast2sms.com/dev/bulkV2"
    params = {
        'authorization' : 'yJOMrPGQYoTKAtved360a7qL5VExRzmgSubZkjDXpHNFcUnh242nYibCwjLu5qM7zZfD0mETh6rUvBP9',
        'sender_id' : "TXTIND",
        'message' : "message",
        'language' : "english",
        'route' : "v3",
        'numbers' : "number"
    }

    response = requests.get(url, params=params)
    dic = response.json()
    print(dic)


    send_sms("1111122222","This is message sent with a python code")