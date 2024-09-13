from functools import partial
from toolz import pipe
from repository.json_repository import (read_json, convert_from_json_to_pilot,
                                        convert_from_json_to_aircraft)

PILOTS_FILE_PATH = "/assets/all_cities_details.json"
AIRCRAFT_FILE_PATH = "./assets/pilots.json"
print(read_json(PILOTS_FILE_PATH))

pilots = pipe(
    PILOTS_FILE_PATH,
    read_json,
    partial(map, convert_from_json_to_pilot),
    list,
)

aircraft = pipe(
    AIRCRAFT_FILE_PATH,
    read_json,
    partial(map, convert_from_json_to_aircraft),
    list
)
