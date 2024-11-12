import json
import os
from math import log2
from typing import List

import geojson
import mapbox
import requests
from requests import Response

from src.country import Country

assert mapbox.Geocoder().session.params['access_token'] == os.environ['MAPBOX_ACCESS_TOKEN']


def staticMapWithBB(country: Country, style=("mapbox", "dark-v10"), res=(720, 1080)) -> Response:
    return requests.get(
        f"https://api.mapbox.com/styles/v1/{style[0]}/{style[1]}/static/{list(country.bbox(True))}/{res[0]}x{res[1]}"
        f"?access_token={os.environ["MAPBOX_ACCESS_TOKEN"]}")


def getMap(country: Country, path: str) -> int:
    # print(mapbox.Geocoder().forward("fi").content
    response = staticMapWithBB(country)
    if "image" in response.headers["Content-Type"]:
        with open(path, "wb") as img:
            return img.write(response.content)
    with open("./data/error.txt", "wb") as img:
        return img.write(response.content)
