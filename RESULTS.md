# Worley Noise Benchmarking
> CPU: AMD Ryzen 7 5700X3D 8-Core Processor (3.00 GHz) |
> GPU: AMD Radeon RX 6600 |
> approx. RAM: 32694 MB |
> approx. VRAM: 8146 MB |
> Width: 1000; Height: 1000; Number of points: 100 |
> 12 programs, 11 runs each (1st run is discarded and not included)

---

## Summary
> run - total, avg, min and max (sorted by avg)

1. Python *with compushady* **(GPU)** - `14.015ms`, `1.402ms`, `1.391ms` and `1.407ms`.
2. Python *with zengl* **(GPU)** - `47.674ms`, `4.767ms`, `4.565ms` and `5.341ms`.
3. C# *with ComputeSharp* **(GPU)** - `79.945ms`, `7.994ms`, `7.854ms` and `8.276ms`.
4. C++ *with no library* **(CPU)** - `91.001ms`, `9.100ms`, `6.565ms` and `12.819ms`.
5. Zig *with zigimg* **(CPU)** - `303.923ms`, `30.392ms`, `30.166ms` and `30.734ms`.
6. Rust *with image* **(CPU)** - `663.393ms`, `66.339ms`, `66.058ms` and `66.631ms`.
7. C# *with ImageSharp* **(CPU)** - `1.549s`, `154.925ms`, `152.250ms` and `157.569ms`.
8. Go *with image* **(CPU)** - `1.925s`, `192.548ms`, `192.165ms` and `193.575ms`.
9. Java *with java.awt.image* **(CPU)** - `2.838s`, `283.770ms`, `282.269ms` and `285.572ms`.
10. Python *with Numba* **(CPU)** - `5.301s`, `530.095ms`, `527.571ms` and `535.292ms`.
11. Typescript *with node-canvas* **(CPU)** - `17.841s`, `1.784s`, `1.773s` and `1.806s`.
12. Python *with Pillow* **(CPU)** - `03:38min`, `21.830s`, `20.931s` and `24.661s`.

---

## All runs
> run - timings (sorted by avg)

1. Python *with compushady* **(GPU)** - `1.401ms`, `1.400ms`, `1.404ms`, `1.403ms`, `1.401ms`, `1.404ms`, `1.400ms`, `1.391ms`, `1.404ms` and `1.407ms`.
2. Python *with zengl* **(GPU)** - `4.975ms`, `4.583ms`, `5.341ms`, `4.565ms`, `4.823ms`, `4.851ms`, `4.647ms`, `4.596ms`, `4.595ms` and `4.697ms`.
3. C# *with ComputeSharp* **(GPU)** - `7.945ms`, `8.276ms`, `7.951ms`, `7.997ms`, `7.941ms`, `7.854ms`, `7.960ms`, `8.025ms`, `8.083ms` and `7.911ms`.
4. C++ *with no library* **(CPU)** - `10.379ms`, `12.819ms`, `9.773ms`, `10.570ms`, `10.097ms`, `8.423ms`, `6.565ms`, `7.780ms`, `6.873ms` and `7.722ms`.
5. Zig *with zigimg* **(CPU)** - `30.401ms`, `30.389ms`, `30.185ms`, `30.734ms`, `30.396ms`, `30.398ms`, `30.166ms`, `30.389ms`, `30.174ms` and `30.692ms`.
6. Rust *with image* **(CPU)** - `66.091ms`, `66.059ms`, `66.631ms`, `66.110ms`, `66.087ms`, `66.596ms`, `66.630ms`, `66.567ms`, `66.565ms` and `66.058ms`.
7. C# *with ImageSharp* **(CPU)** - `154.390ms`, `154.481ms`, `154.407ms`, `153.990ms`, `154.949ms`, `156.071ms`, `155.768ms`, `155.377ms`, `157.569ms` and `152.250ms`.
8. Go *with image* **(CPU)** - `192.165ms`, `193.575ms`, `192.165ms`, `193.166ms`, `192.666ms`, `192.650ms`, `192.165ms`, `192.165ms`, `192.599ms` and `192.165ms`.
9. Java *with java.awt.image* **(CPU)** - `282.269ms`, `285.220ms`, `282.580ms`, `282.352ms`, `285.098ms`, `283.302ms`, `283.294ms`, `285.572ms`, `283.376ms` and `284.637ms`.
10. Python *with Numba* **(CPU)** - `531.275ms`, `528.302ms`, `530.504ms`, `528.482ms`, `528.575ms`, `535.292ms`, `527.846ms`, `530.883ms`, `527.571ms` and `532.220ms`.
11. Typescript *with node-canvas* **(CPU)** - `1.793s`, `1.785s`, `1.781s`, `1.806s`, `1.781s`, `1.776s`, `1.773s`, `1.783s`, `1.780s` and `1.784s`.
12. Python *with Pillow* **(CPU)** - `21.756s`, `21.759s`, `21.865s`, `21.455s`, `21.978s`, `21.234s`, `21.269s`, `21.395s`, `20.931s` and `24.661s`.

---

## Stats

- total time taken: `05:58min`.
- total time taken (just runs): `04:08min`.
- best avg: Python *with compushady* **(GPU)** `(1.402ms)`.
- worst avg: Python *with Pillow* **(CPU)** `(21.830s)`.
