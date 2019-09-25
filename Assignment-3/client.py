import requests
import json
import zeep


def api():
    res = requests.get('http://localhost:5000').content.decode('utf-8')
    res = json.loads(res)
    print(res)

def post_api():
    payload = {'key1': 1, 'key2': 2}
    res = requests.post('http://localhost:5000', data=json.dumps(payload)).content.decode('utf-8')
    # res = json.loads(res)
    print(res)

def soap():
    wsdl = 'http://localhost:8080/service/calculator.wsdl'
    client = zeep.Client(wsdl)
    # with client.settings(raw_response=True):
    print(client.service.Calculator(11.2, '*', 2))

# def soap():
#     wsdl = 'http://localhost:8080/service/calculator.wsdl'
#     client = zeep.Client(wsdl)
#     with client.settings(raw_response=True):
#         print(client.service.StudentDetails('Sajal','11').content)

# post_api()
soap()