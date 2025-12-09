# pyright: reportMissingTypeStubs=false

import math
import os
from random import choice, randint
from string import ascii_letters, digits
from sys import argv
from time import perf_counter_ns

import numpy as np
from numba import njit  # pyright: ignore[reportUnknownVariableType]
from PIL import Image


@njit
def generate(width: int, height: int, points: np.ndarray, /) -> np.ndarray:
    pixels = np.zeros(width * height, dtype=np.uint8)

    for y in range(height):
        for x in range(width):
            min_dist = 1e30

            for p in points:
                dx = x - p[0]
                dy = y - p[1]
                min_dist = min(min_dist, dx * dx + dy * dy)

            dist = int(math.sqrt(min_dist))

            if dist < 0:
                dist = 0
            elif dist > 255:
                dist = 255

            pixels[y * width + x] = 255 - dist

    return pixels


chars = ascii_letters + digits


def random_characters(length: int = 10, /) -> str:
    return "".join(choice(chars) for _ in range(length))


width = int(argv[1])
height = int(argv[2])
number_of_points = int(argv[3])
save_image = argv[4] == "true"

image = Image.new("L", (width, height))
points = np.array(
    [(randint(0, width), randint(0, height)) for _ in range(number_of_points)],
    dtype=np.int32,
)

start = perf_counter_ns()

data = generate(width, height, points)

end = perf_counter_ns()

print(end - start)

if not save_image:
    exit()

if not os.path.exists("img/"):
    os.mkdir("img/")

image.putdata(data)
image.save(f"img/{random_characters()}.png")
