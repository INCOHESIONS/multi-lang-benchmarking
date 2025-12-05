import os
import struct
from ctypes import c_double, sizeof
from itertools import chain as flatten
from random import choice, uniform
from string import ascii_letters, digits
from sys import argv
from time import perf_counter

import zengl
from PIL import Image

chars = ascii_letters + digits


def random_characters(length: int = 10, /) -> str:
    return "".join(choice(chars) for _ in range(length))


width = int(argv[1])
height = int(argv[2])
number_of_points = int(argv[3])
save_image = argv[4] == "true"

VERTEX_SHADER = """
    #version 330 core

    vec2 positions[3] = vec2[](
        vec2(-1.0, -1.0),
        vec2(3.0, -1.0),
        vec2(-1.0, 3.0)
    );

    void main() {
        gl_Position = vec4(positions[gl_VertexID], 0.0, 1.0);
    }
"""

FRAGMENT_SHADER = """
    #version 330 core
    #include "points"

    const float INFINITY = 3.402823466e+38F;

    layout (std140) uniform Points {
        vec2 points[numberOfPoints];
    };

    in vec3 v_color;

    layout (location = 0) out vec4 out_color;

    void main() {
        float minDist = INFINITY;

        for (int i = 0; i < numberOfPoints; i++)
            minDist = min(minDist, dot(points[i] - gl_FragCoord.xy, points[i] - gl_FragCoord.xy));

        float color = 1.0 - sqrt(minDist) / 255.0;

        out_color = vec4(color, color, color, 1.0);
    }
"""

zengl.init(zengl.loader(headless=True))  # pyright: ignore[reportUnknownMemberType]

ctx = zengl.context()
image = ctx.image((width, height), "rgba8unorm", texture=False)
points = ctx.buffer(size=number_of_points * 2 * sizeof(c_double), uniform=True)
pipeline = ctx.pipeline(
    vertex_shader=VERTEX_SHADER,
    fragment_shader=FRAGMENT_SHADER,
    framebuffer=[image],
    topology="triangles",
    includes={
        "points": f"const int numberOfPoints = {number_of_points};",
    },
    layout=[
        {
            "name": "Points",
            "binding": 0,
        },
    ],
    resources=[
        {
            "type": "uniform_buffer",
            "binding": 0,
            "buffer": points,
        },
    ],
    vertex_count=3,
)

points.write(
    struct.pack(
        f"{number_of_points * 2}f",
        *flatten(
            *((uniform(0, width), uniform(0, height)) for _ in range(number_of_points))
        ),
    )
)

start = perf_counter()

ctx.new_frame()
image.clear()
pipeline.render()
ctx.end_frame()

end = perf_counter()

print(end - start)

if not save_image:
    exit()

img = Image.frombuffer("RGBA", image.size, image.read(), "raw", "RGBA", 0, -1)  # pyright: ignore[reportUnknownMemberType]

if not os.path.exists("img/"):
    os.mkdir("img/")

img.save(f"img/{random_characters()}.png")
