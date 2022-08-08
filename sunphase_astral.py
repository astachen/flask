from astral import LocationInfo
import datetime
from astral.sun import sun


def city_astral():
    # in the future, this will be moved to the url
    name = input('Please type the name here:')

    # put the tuple into the dictionary
    LocationInfos = {'Beijing': ("Beijing", "China", "Asia/Shanghai", 39.904211, 116.407395),
                     'Shanghai': ("Shanghai", "China", "Asia/Shanghai", 31.231707, 121.472641)}

    # get the data from the dictionary
    city = LocationInfo(LocationInfos[name])

    # these are the test codes of line 13
    print((
        f"Information for {city.name}/{city.region}\n"
        f"Timezone: {city.timezone}\n"
        f"Latitude: {city.latitude:.02f}; Longitude: {city.longitude:.02f}\n"
    ))

    # this will print the sunrise time
    s = sun(city.observer, date=datetime.date(2022, 8, 7), tzinfo='Asia/Shanghai')
    print(f'Sunrise: {s["sunrise"]}\n')


if __name__ == '__main__':
    city_astral()
