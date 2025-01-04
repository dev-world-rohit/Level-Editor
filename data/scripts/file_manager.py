import json

def read_json(path, is_json = False):
    path = "data/" + path
    file = open(path, 'r')
    if is_json:
        data = json.loads(file.read())
    else:
        data = file.read()
    return data

def write_json(path, data, is_json = False):
    path = "data/" + path
    file = open(path, "w")
    if is_json:
        data = json.dumps(data)
    file.write(data)
    return True
