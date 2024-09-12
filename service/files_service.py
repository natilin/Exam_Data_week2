import os

from api.weather_api import get_cities_details, get_cities_weather, get_city_details
from repository.json_repository import read_json, create_json_file

TARGETS = read_json("assets/targets.json")

def create_files_if_not_exist():
    if not os.path.isfile("assets/all_cities_details.json"):
        cities_details = get_cities_details(TARGETS)
        create_json_file(cities_details, "all_cities_details")

    if not os.path.isfile("assets/all_cities_weather.json"):
        cities_weather = get_cities_weather(TARGETS)
        create_json_file(cities_weather, "all_cities_weather")

    if not os.path.isfile("assets/tel-aviv detail.json"):
        isreal_details = get_city_details("tel%aviv")
        create_json_file(isreal_details, "tel-aviv detail")
