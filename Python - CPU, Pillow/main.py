import os
from math import isqrt
from random import choice, randint
from string import ascii_letters, digits
from sys import argv
from time import perf_counter_ns

from PIL import Image

chars = ascii_letters + digits


def random_characters(length: int = 10, /) -> str:
    return "".join(choice(chars) for _ in range(length))


def squared_dist(p: tuple[int, int], x: int, y: int) -> int:
    dx = x - p[0]
    dy = y - p[1]
    return dx * dx + dy * dy


def clamp(value: int, minimum: int, maximum: int, /) -> int:
    return max(min(value, maximum), minimum)


width = int(argv[1])
height = int(argv[2])
number_of_points = int(argv[3])
save_image = argv[4] == "true"

image = Image.new("L", (width, height))
points = tuple((randint(0, width), randint(0, height)) for _ in range(number_of_points))

start = perf_counter_ns()

data = [
    255 - clamp(min(isqrt(squared_dist(p, x, y)) for p in points), 0, 255)
    for x in range(width)
    for y in range(height)
]

end = perf_counter_ns()

print(end - start)

if not save_image:
    exit()

if not os.path.exists("img/"):
    os.mkdir("img/")

image.putdata(data)
image.save(f"img/{random_characters()}.png")
