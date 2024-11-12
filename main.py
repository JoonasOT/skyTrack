from src.planes import getPlanes
from src.map import getMap, featureAtLatLon
from src.country import getCountry


def main():
    country = getCountry("IT")
    print(country)
    planes = getPlanes(country)
    print(planes)
    print(getMap(country))


if __name__ == "__main__":
    main()
