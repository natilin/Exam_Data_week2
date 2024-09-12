import json


def create_json_file(json_var, name):
    json_str = json.dumps(json_var)
    json_file = open(name + ".json", "w")
    json_file.write(json_str)
    json_file.close()

