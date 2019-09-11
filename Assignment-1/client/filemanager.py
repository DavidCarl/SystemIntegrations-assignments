import json


def load_data(filepath):
    data = {}
    with open(filepath, 'r') as f:
        data = json.load(f)
    return data

def save_data(filepath, data):
    with open(filepath, 'w') as f:
        f.write(json.dumps(data, indent=4, sort_keys=True))