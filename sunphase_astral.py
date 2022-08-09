from astral import LocationInfo
import datetime
from astral.sun import sun


def city_astral(name):
    # reformat the name
    name = name.strip().capitalize()

    # put the tuple into the dictionary
    LocationInfos = {'Beijing': ("Beijing", "China", "Asia/Shanghai", 39.904211, 116.407395),
                     'Shanghai': ("Shanghai", "China", "Asia/Shanghai", 31.231707, 121.472641)}

    # input error check
    if name not in LocationInfos:
        return 'city not found'

    # read the tuple from the dictionary and divide it
    name, region, timezone, latitude, longitude = LocationInfos[name]

    # initialize data to compute the sunrise time
    city = LocationInfo(name, region, timezone, latitude, longitude)

    # this will print the sunrise time
    s = sun(city.observer, date=datetime.date(2022, 8, 9), tzinfo=timezone)

    return f'{s["sunrise"]} {timezone} {name}'
