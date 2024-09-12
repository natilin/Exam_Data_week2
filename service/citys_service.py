from toolz import pipe, first, get_in, partial
from operator import  itemgetter

extract_location = lambda dict: pipe(
    dict,
    first,
    lambda x: (x["lat"], x["lon"])
)


extract_weather = lambda d: pipe(
    d,
    itemgetter("list"),
    partial(filter, lambda x: "00:00:00" in x["dt_txt"]),
    next
)



