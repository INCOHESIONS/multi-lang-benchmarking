# pyright: reportMissingTypeStubs=false, reportUnknownArgumentType=false, reportUnknownMemberType=false, reportUnknownVariableType=false
# ^ prevents a ton of type checking errors as compushady lacks stubs

import os
import struct
from ctypes import c_int, sizeof
from itertools import chain as flatten
from random import choice, randint
from string import ascii_letters, digits
from sys import argv
from time import perf_counter

import compushady
from compushady.formats import B8G8R8A8_UNORM, R32G32_UINT
from compushady.shaders.hlsl import compile
from PIL import Image  # type: ignore

compushady.config.set_debug(True)

chars = ascii_letters + digits


def random_characters(length: int = 10, /) -> str:
    return "".join(choice(chars) for _ in range(length))


def round_to_nearest_larger_power_of_2(n: int, /) -> int:
    v = 1

    while v < n:
        v *= 2

    return v


width = int(argv[1])
height = int(argv[2])
number_of_points = int(argv[3])
save_image = argv[4] == "true"

SHADER = f"""
    #define INFINITY 3.402823466e+38F

    RWTexture2D<float4> target;
    Buffer<uint2> points;

    [numthreads(8, 8, 1)]
    void main(uint3 tid : SV_DispatchThreadID)
    {{
        float minDist = INFINITY;

        for (uint i = 0; i < {number_of_points}; i++)
            minDist = min(minDist, dot(points[i] - tid.xy, points[i] - tid.xy));

        const float color = 1.0F - clamp(sqrt(minDist), 0.0F, 255.0F) / 255.0F;

        target[tid.xy] = float4(color, color, color, 1.0F);
    }}
"""

texture_width = round_to_nearest_larger_power_of_2(width)
texture_height = round_to_nearest_larger_power_of_2(height)

target = compushady.Texture2D(texture_width, texture_height, format=B8G8R8A8_UNORM)

staging = compushady.Buffer(
    number_of_points * 2 * sizeof(c_int), compushady.HEAP_UPLOAD
)

points = compushady.Buffer(staging.size, format=R32G32_UINT)

staging.upload(
    struct.pack(
        f"{number_of_points * 2}I",
        *flatten(
            *((randint(0, width), randint(0, height)) for _ in range(number_of_points))
        ),
    )
)
staging.copy_to(points)

compute = compushady.Compute(compile(SHADER), uav=[target], srv=[points])

start = perf_counter()

compute.dispatch(texture_width // 8, texture_height // 8, 1)

end = perf_counter()
print(end - start)

if not save_image:
    exit()

readback = compushady.Buffer(target.size, compushady.HEAP_READBACK)
target.copy_to(readback)

image = Image.frombuffer(
    "RGBA",
    (texture_width, texture_height),
    readback.readback(),  # pyright: ignore[reportArgumentType]
)

image = image.crop((0, 0, width, height))

if not os.path.exists("img/"):
    os.mkdir("img/")

image.save(f"img/{random_characters()}.png")
