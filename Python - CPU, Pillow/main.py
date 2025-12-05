import os
from math import hypot
from random import randint
from sys import argv
from time import perf_counter

from PIL import Image  # type: ignore


def clamp(value: int, minimum: int, maximum: int, /) -> int:
    return max(min(value, maximum), minimum)


width = int(argv[1])
height = int(argv[2])
number_of_points = int(argv[3])
save_image = argv[4] == "true"

image = Image.new("L", (width, height))
points = tuple((randint(0, width), randint(0, height)) for _ in range(number_of_points))

start = perf_counter()

image.putdata(  # pyright: ignore[reportUnknownMemberType]
    [
        255 - clamp(min(int(hypot(x - p[0], y - p[1])) for p in points), 0, 255)
        for x in range(width)
        for y in range(height)
    ]
)

end = perf_counter()

print(end - start)

if not save_image:
    exit()

if not os.path.exists("img/"):
    os.mkdir("img/")

image.save("img/image.png")
