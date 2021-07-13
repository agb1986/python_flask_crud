import json as j


def get_data():
    with open('./users.json', 'r') as d:
        return j.loads(d.read())


def write_data(data):
    with open('./users.json', 'w') as d:
        j.dump(data, d)
