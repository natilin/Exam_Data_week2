from service.citys_service import (extract_location,
                                   extract_weather)
from api.weather_api import get_cities_weather, get_cities_details, get_city_details
from repository.json_repository import create_json_file, read_json
from toolz import get_in

CITIES_WEATHER = read_json("assets/all_cities_weather.json")



def main():
    # cities_details = get_cities_details(TARGETS)
    # cities_weather = get_cities_weather(TARGETS)
    # create_json_file(cities_details, "all_cities_details")
    # create_json_file(cities_weather, "all_cities_weather")
    isreal_details = get_city_details("tel%aviv")
    create_json_file(isreal_details, "tel-aviv detail")











if __name__ == '__main__':
    main()