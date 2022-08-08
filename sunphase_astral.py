from astral import LocationInfo
import datetime
from astral.sun import sun


def city_astral(name):

    # put the tuple into the dictionary
    LocationInfos = {'Beijing': ("Beijing", "China", "Asia/Shanghai", 39.904211, 116.407395),
                     'Shanghai': ("Shanghai", "China", "Asia/Shanghai", 31.231707, 121.472641)}

    # read the tuple from the dictionary and divide it
    name, region, timezone, latitude, longitude = LocationInfos[name]

    # initialize data to compute the sunrise time
    city = LocationInfo(name, region, timezone, latitude, longitude)

    # these are the test codes of line 18, it will be deleted in the future
    print((
        f"Information for {name}/{region}\n"
        f"Timezone: {timezone}\n"
        f"Latitude: {latitude:.02f}; Longitude: {longitude:.02f}\n"
    ))

    # this will print the sunrise time
    s = sun(city.observer, date=datetime.date(2022, 8, 7), tzinfo=timezone)
    print(f'Sunrise: {s["sunrise"]}\n')

    return s
