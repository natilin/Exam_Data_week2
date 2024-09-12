import math


"""
The weather is based on 3 parameters:
wind speed, cloud level and weather conditions
"""

def weather_condition_score(weather):
    if weather == "Clear":
        return 1.0
    elif weather == "Clouds":
        return 0.7
    elif weather == "Rain":
        return 0.4
    elif weather == "Stormy":
        return 0.2
    else:
        return 0


#מחשב את רמת העננים, אם מעונן מלא מחזיר 0 אם בהיר מחזיר  1
weather_cloud_score = lambda x: 100 - x / 100

#חישוב הרוח מבוסס על סולם מ1 עד 12 (סולם בופר)
weather_wind_score = lambda x: 1 - (x / 12)

total_weather_score = lambda a, b, c: sum([a, b, c]) / 3



def haversine_distance(lat1, lon1, lat2, lon2):
    r = 6371.0  # Radius of the Earth in kilometers
    # Convert degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = r * c
    return distance





# print(haversine_distance(33.5130695, 36.3095814,32.0852997, 34.7818064 ))



