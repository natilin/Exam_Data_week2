import requests
from toolz import partial, reduce


API_KEY = "ce6f3e5df2f5cfa7df1f7c5564758fe4"


def make_request_by_api_key(api_key, url):
    url = f"{url}&appid={api_key}"
    response = requests.request("GET", url, verify=False)
    return response.json()


make_request = partial(make_request_by_api_key, API_KEY)


def get_city_details(city):
    url = f"https://api.openweathermap.org/geo/1.0/direct?q=" + city
    return make_request(url)


def get_city_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q=" + city
    return make_request(url)


get_cities_weather = lambda lst: [get_city_weather(target["city"]) for target in lst]
get_cities_details = lambda lst: [get_city_details(target["city"])[0] for target in lst]


