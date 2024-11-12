from PIL import Image
from PIL.ImageDraw import ImageDraw


def process(path: str, bbox: tuple[float, float, float, float], planes: list) -> None:
    with Image.open(path) as img:
        draw = ImageDraw(img)

        minx, miny, maxx, maxy = bbox
        maxx = maxx - minx
        maxy = maxy - miny

        locations: list[tuple] = []
        for plane in planes:
            diffx = (plane.longitude - minx) / maxx
            diffy = (plane.latitude - miny) / maxy
            locations.append(((diffx, diffy), plane))

        xmax, ymax = img.size
        for location in locations:
            loc, plane = location
            x, y = loc
            pos = (x * xmax, (1-y) * ymax)
            draw.circle(pos, radius=4, fill=(255, 255, 255))
        img.show()
