from astral import LocationInfo

city = LocationInfo("Beijing", "China", "Asia/Shanghai", 39.904211, 116.407395)
print((
    f"Information for {city.name}/{city.region}\n"
    f"Timezone: {city.timezone}\n"
    f"Latitude: {city.latitude:.02f}; Longitude: {city.longitude:.02f}\n"
))
