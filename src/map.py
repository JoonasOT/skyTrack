import os

import mapbox

from src.country import Country

assert mapbox.Geocoder().session.params['access_token'] == os.environ['MAPBOX_ACCESS_TOKEN']


def featureAtLatLon(lat: float, lon: float):
    return {
        'type': 'Feature',
        'properties': {},
        'geometry': {
            'type': 'Point',
            'coordinates': [lon, lat]
        }
    }


def getMap(country: Country, features=None) -> int:
    print(F"Lon & lat: {(country.lon(), country.lat())}")
    response = mapbox.StaticStyle().image(username="mapbox", style_id="dark-v10",
                                          lon=country.lon(), lat=country.lat(), zoom=4.8, pitch=0.0,
                                          width=720, height=1080, features=features
                                          )
    if "image" in response.headers["Content-Type"]:
        with open("./data/map.png", "wb") as img:
            return img.write(response.content)
    with open("./data/map_error.txt", "wb") as img:
        return img.write(response.content)
