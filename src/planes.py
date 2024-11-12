import os
from opensky_api import OpenSkyApi, OpenSkyStates   # https://github.com/openskynetwork/opensky-api.git

from src.country import Country

OPENSKY_API = OpenSkyApi(os.environ['OPENSKY_API_USERNAME'], os.environ['OPENSKY_API_PASSWORD'])


def getPlanes(country: Country) -> OpenSkyStates:
    return OPENSKY_API.get_states(bbox=country.bbox())
