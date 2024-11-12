from src.planes import getPlanes
from src.map import getMap, featureAtLatLon
from src.country import getCountry


def main():
    country = getCountry("FI")
    print(country)
    planes = getPlanes(country)
    print(planes)
    print(getMap(country,  [featureAtLatLon(plane.latitude, plane.longitude) for plane in planes.states]))


if __name__ == "__main__":
    main()
