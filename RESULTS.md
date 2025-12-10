# Worley Noise Benchmarking
> CPU: AMD Ryzen 7 5700X3D 8-Core Processor (3.00 GHz) |
> GPU: AMD Radeon RX 6600 |
> approx. RAM: 32694 MB |
> approx. VRAM: 8146 MB |
> Width: 1000; Height: 1000; Number of points: 100 |
> 12 programs, 11 runs each (1st run is discarded and not included)
> Data gathered on ['2025-12-10T02:23:16', '630817+00:00']Z

---

## Summary
> sorted by avg, diffs based on avg

|  Program  |  Average  |  Min  |  Max  |   Total   | Range |  Diff. from #1  | Diff. from Previous |
|-----------|:---------:|:-----:|:-----:|:---------:|:------|:---------------:|:-------------------:|
| Python *with compushady* **(GPU)** | `1.340ms` | `1.294ms` | `1.368ms` | `13.402ms` | 73.700µs | - | - |
| Python *with zengl* **(GPU)** | `4.733ms` | `4.319ms` | `4.947ms` | `47.334ms` | 627.600µs | 3.53x | 3.53x |
| C# *with ComputeSharp* **(GPU)** | `8.099ms` | `7.901ms` | `8.313ms` | `80.987ms` | 412.300µs | 6.04x | 1.71x |
| C++ *with no library* **(CPU)** | `8.475ms` | `6.174ms` | `15.522ms` | `84.751ms` | 9.348ms | 6.32x | 1.05x |
| Zig *with zigimg* **(CPU)** | `30.792ms` | `30.168ms` | `31.348ms` | `307.924ms` | 1.180ms | 22.98x | 3.63x |
| Rust *with image* **(CPU)** | `65.925ms` | `65.261ms` | `66.619ms` | `659.254ms` | 1.358ms | 49.19x | 2.14x |
| C# *with ImageSharp* **(CPU)** | `156.821ms` | `152.707ms` | `161.205ms` | `1.568s` | 8.498ms | 117.02x | 2.38x |
| Go *with image* **(CPU)** | `192.415ms` | `191.664ms` | `193.666ms` | `1.924s` | 2.002ms | 143.58x | 1.23x |
| Java *with java.awt.image* **(CPU)** | `282.982ms` | `280.484ms` | `285.217ms` | `2.830s` | 4.733ms | 211.16x | 1.47x |
| Python *with Numba* **(CPU)** | `534.974ms` | `529.027ms` | `544.489ms` | `5.350s` | 15.462ms | 399.19x | 1.89x |
| Typescript *with node-canvas* **(CPU)** | `1.807s` | `1.784s` | `1.844s` | `18.068s` | 60.530ms | 1348.22x | 3.38x |
| Python *with Pillow* **(CPU)** | `21.351s` | `21.085s` | `21.597s` | `03:33min` | 511.928ms | 15931.46x | 11.82x |

---

## Stats

- total time taken: `05:37min`.
- total time taken (just runs): `04:04min`.
- best avg: Python *with compushady* **(GPU)** `(1.340ms)`.
- worst avg: Python *with Pillow* **(CPU)** `(21.351s)`.
