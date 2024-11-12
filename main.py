from src.planes import getPlanes
from src.map import getMap
from src.country import getCountry
from src.imageprocessing import *


def main():
    country = getCountry("FI")
    print(country)
    planes = getPlanes(country)
    print(planes)
    print(getMap(country, "./data/map.png"))
    process("./data/map.png", country.bbox(minFirst=True), [plane for plane in planes.states])


if __name__ == "__main__":
    main()
