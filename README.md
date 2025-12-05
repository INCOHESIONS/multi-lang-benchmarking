# Multi-language Worley Noise Benchmarking

This project aims to implement the same algorithm in multiple different languages, using multiple different libraries, and even in different devices (CPU/GPU), mostly for fun.

The algorithm in question is a simplified version of Worley/Voronoi Noise, that isn't based in cells or anything fancy. Just plop some points on the screen, and calculate the distance from each pixel to the nearest point.

## How to run it

Here are the recommended versions of all the tools needed to run all the currently available versions of the program:

- .NET 10+
- Bun 1.3.3+
- Clang 21.1.6+ (or any version or compiler that supports C++23)
- Go 1.25+
- Java 24+
- Python 3.14+
- Rust 1.84+
- Zig 0.15.2+

All folders should have a file that indicate the dependencies required to run the program (`requirements.txt` for Python, `.csproj` for C#, `Cargo.toml` for Rust, etc) and if they don't, they simply require no dependencies (Java) or the dependecies are bundled (C++).

## How it works

Every folder has a `run.bat` script, and, optionally, a `prepare.bat` script. All implementations must output the time they took to execute the primary part of the code (the actual image generation, not the point generation or the whole time it took to execute the program) in seconds, as a float.

`benchmarking.py` then loops through each directory, executing `prepare.bat`, which may compile, preferably with optimizations, the program in the folder. Then, it executes `run.bat` with 4 arguments: width, height, number of points, and a boolean indicating whether to save the image into an /img/ folder or not. It executes each program 11 times by default, discarding the first output, as it simply serves as a warm-up round and allows languages to perform caching.

Then, after tallying all the outputs, the program generates a `RESULTS.md` containing information about the system, how long each program and run took, and other stats.
