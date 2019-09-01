import json


def load_data():
    data = {}
    with open('customer.json', 'r') as f:
        data = json.load(f)
    return data

def save_data(data):
    with open('customer.json', 'w') as f:
        f.write(json.dumps(data, indent=4, sort_keys=True))