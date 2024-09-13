import json
from model.aircraft import Aircraft
from model.pilot import Pilot


def create_json_file(jsn, name):
    json_str = json.dumps(jsn)
    json_file = open("./assets/" + name + ".json", "w", encoding="utf-8")
    json_file.write(json_str)
    json_file.close()


def read_json(path):
    try:
        with open(path, 'r') as file:
            return json.load(file)
    except Exception as e:
        print(e)
        return []


def convert_from_json_to_pilot(jsn):
    pilot = Pilot(jsn["name"], jsn["skill"])
    return pilot


def convert_from_json_to_aircraft(jsn):
    aircraft = Aircraft(jsn["type"], jsn["speed"], jsn["fuel_capacity"])
    return aircraft
