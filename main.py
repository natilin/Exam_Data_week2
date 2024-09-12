from service.citys_service import (extract_location,
                                   extract_weather)
from api.weather_api import get_cities_weather, get_cities_details, get_city_details
from repository.json_repository import create_json_file, read_json
from toolz import get_in
from service.files_service import create_files_if_not_exist

CITIES_WEATHER = read_json("assets/all_cities_weather.json")


def main():
    create_files_if_not_exist()


if __name__ == '__main__':
    main()