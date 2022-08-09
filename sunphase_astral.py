from astral import LocationInfo
import datetime
from astral.sun import sun


def city_astral(name):
    # reformat the name
    name = name.strip().capitalize()

    # put the tuple into the dictionary
    LocationInfos = {'Beijing': ("Beijing", "China", "Asia/Shanghai", 116.407395, 39.904211),
                     'Shanghai': ("Shanghai", "China", "Asia/Shanghai", 121.472641, 31.231707),
                     'Shenyang': ("Shenyang", "China", "Asia/Shanghai", 123.429092, 41.796768),
                     'Changchun': ("Changchun", "China", "Asia/Shanghai", 125.324501, 43.886841),
                     'Harbin': ("Harbin", "China", "Asia/Shanghai", 126.642464, 45.756966),
                     'Tianjin': ("Tianjin", "China", "Asia/Shanghai", 117.190186, 39.125595),
                     'Hohhot': ("Hohhot", "China", "Asia/Shanghai", 111.751990, 40.841490),
                     'Yinchuan': ("Yinchuan", "China", "Asia/Shanghai", 106.232480, 38.486440),
                     'Taiyuan': ("Taiyuan", "China", "Asia/Shanghai", 112.549248, 37.857014),
                     'Shijiazhuang': ("Shijiazhuang", "China", "Asia/Shanghai", 114.502464, 38.045475),
                     'Jinan': ("Jinan", "China", "Asia/Shanghai", 117.000923, 36.675808),
                     'Zhengzhou': ("Zhengzhou", "China", "Asia/Shanghai", 113.665413, 34.757977),
                     'Xian': ("Xian", "China", "Asia/Shanghai", 108.948021, 34.263161),
                     'Wuhan': ("Wuhan", "China", "Asia/Shanghai", 114.298569, 30.584354),
                     'Nanjing': ("Nanjing", "China", "Asia/Shanghai", 118.76741, 32.041546),
                     'Hefei': ("Hefei", "China", "Asia/Shanghai", 117.283043, 31.861191),
                     'Changsha': ("Changsha", "China", "Asia/Shanghai", 112.982277, 28.19409),
                     'Nanchang': ("Nanchang", "China", "Asia/Shanghai", 115.892151, 28.676493),
                     'Hangzhou': ("Hangzhou", "China", "Asia/Shanghai", 120.15358, 30.287458),
                     'Fuzhou': ("Fuzhou", "China", "Asia/Shanghai", 119.306236, 26.075302),
                     'Guangzhou': ("Guangzhou", "China", "Asia/Shanghai", 113.28064, 23.125177),
                     'Taipei': ("Taipei", "China", "Asia/Shanghai", 121.5200760, 25.0307240),
                     'Haikou': ("Haikou", "China", "Asia/Shanghai", 110.199890, 20.044220),
                     'Nanning': ("Nanning", "China", "Asia/Shanghai", 108.320007, 22.82402),
                     'Chongqing': ("Chongqing", "China", "Asia/Shanghai", 106.504959, 29.533155),
                     'Kunming': ("Kunming'", "China", "Asia/Shanghai", 102.71225, 25.040609),
                     'Guiyang': ("Guiyang", "China", "Asia/Shanghai", 106.713478, 26.578342),
                     'Chengdu': ("Chengdu", "China", "Asia/Shanghai", 104.065735, 30.659462),
                     'Lanzhou': ("Lanzhou", "China", "Asia/Shanghai", 103.834170, 36.061380),
                     'Xining': ("Xining", "China", "Asia/Shanghai", 101.777820, 36.617290),
                     'Lhasa': ("Lhasa", "China", "Asia/Shanghai", 91.11450, 29.644150),
                     'Urumqi': ("Urumqi", "China", "Asia/Urumqi", 87.616880, 43.826630),
                     'Hongkong': ("Hongkong", "China", "Asia/Shanghai", 114.165460, 22.275340),
                     'Macao': ("Macao", "China", "Asia/Shanghai", 113.549130, 22.198750)
                     }

    # input error check
    if name not in LocationInfos:
        return 'city not found'

    # read the tuple from the dictionary and divide it
    # the database I get from the internet put the longitude first
    name, region, timezone, longitude, latitude = LocationInfos[name]

    # initialize data to compute the sunrise time
    city = LocationInfo(name, region, timezone, latitude, longitude)

    # this will print the sunrise time
    s = sun(city.observer, date=datetime.date(2022, 8, 9), tzinfo=timezone)

    return f'{s["sunrise"]} {timezone} {name}'
