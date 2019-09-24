import SOAPpy
import requests
import json


# server = SOAPpy.SOAPProxy("http://localhost:8888/")
# print(server.hello())

def api():
    res = requests.get('http://localhost:5000').content.decode('utf-8')
    res = json.loads(res)
    print(res)

def post_api():
    payload = {'key1': 1, 'key2': 2}
    res = requests.post('http://localhost:5000', data=json.dumps(payload)).content.decode('utf-8')
    # res = json.loads(res)
    print(res)

post_api()
