import json


def create_json_file(json_var, name):
    json_str = json.dumps(json_var)
    json_file = open("./assets/" + name + ".json", "w")
    json_file.write(json_str)
    json_file.close()

def read_json(path):
    try:
        with open(path, 'r', encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        print(e)
        return []
