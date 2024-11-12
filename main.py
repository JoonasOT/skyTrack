from src.planes import getPlanes
from src.map import getMap
from src.country import getCountry


def main():
    country = getCountry("FI")
    print(country)
    print(getPlanes(country))
    print(getMap(country))


if __name__ == "__main__":
    main()
