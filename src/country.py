from typing import NamedTuple
from country_bounding_boxes import country_subunits_by_iso_code


class Country(NamedTuple):
    latMin: float
    latMax: float
    lonMin: float
    lonMax: float

    def lat(self) -> float:
        return (5 * self.latMin + 6 * self.latMax) / 11

    def lon(self) -> float:
        return (self.lonMin + self.lonMax) / 2

    def bbox(self, minFirst=False) -> tuple[float, float, float, float]:
        return (self.latMin, self.latMax, self.lonMin, self.lonMax) if not minFirst else (self.lonMin, self.latMin, self.lonMax, self.latMax)


def getCountry(iso_code: str) -> Country:
    countries = list(country_subunits_by_iso_code(iso_code))
    assert len(countries) > 0
    lonMin, latMin, lonMax, latMax = countries[0].bbox
    return Country(latMin, latMax, lonMin, lonMax)
