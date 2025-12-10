# Worley Noise Benchmarking
> CPU: AMD Ryzen 7 5700X3D 8-Core Processor (3.00 GHz) |
> GPU: AMD Radeon RX 6600 |
> approx. RAM: 32694 MB |
> approx. VRAM: 8146 MB |
> Width: 1000; Height: 1000; Number of points: 100 |
> 12 programs, 11 runs each (1st run is discarded and not included)

---

## Summary
> sorted by avg, diffs based on avg

|  Program  |  Average  |  Min  |  Max  |   Total   |  Diff. from #1  | Diff. from Previous. |
|-----------|:---------:|:-----:|:-----:|:---------:|:---------------:|:--------------------:|
| Python *with compushady* **(GPU)** | `1.366ms` | `1.359ms` | `1.396ms` | `13.665ms` | - | - |
| Python *with zengl* **(GPU)** | `5.089ms` | `4.746ms` | `5.190ms` | `50.888ms` | 3.72x | 3.72x |
| C++ *with no library* **(CPU)** | `7.745ms` | `6.172ms` | `12.386ms` | `77.447ms` | 5.67x | 1.52x |
| C# *with ComputeSharp* **(GPU)** | `8.032ms` | `7.867ms` | `8.262ms` | `80.321ms` | 5.88x | 1.04x |
| Zig *with zigimg* **(CPU)** | `30.682ms` | `30.264ms` | `30.945ms` | `306.824ms` | 22.45x | 3.82x |
| Rust *with image* **(CPU)** | `66.245ms` | `65.442ms` | `68.691ms` | `662.446ms` | 48.48x | 2.16x |
| C# *with ImageSharp* **(CPU)** | `156.035ms` | `152.079ms` | `163.089ms` | `1.560s` | 114.19x | 2.36x |
| Go *with image* **(CPU)** | `192.791ms` | `192.063ms` | `194.605ms` | `1.928s` | 141.09x | 1.24x |
| Java *with java.awt.image* **(CPU)** | `284.292ms` | `281.404ms` | `295.998ms` | `2.843s` | 208.05x | 1.47x |
| Python *with Numba* **(CPU)** | `531.179ms` | `528.082ms` | `535.852ms` | `5.312s` | 388.72x | 1.87x |
| Typescript *with node-canvas* **(CPU)** | `1.774s` | `1.751s` | `1.805s` | `17.743s` | 1298.47x | 3.34x |
| Python *with Pillow* **(CPU)** | `21.418s` | `21.005s` | `22.136s` | `03:34min` | 15674.07x | 12.07x |

---

## Stats

- total time taken: `05:43min`.
- total time taken (just runs): `04:04min`.
- best avg: Python *with compushady* **(GPU)** `(1.366ms)`.
- worst avg: Python *with Pillow* **(CPU)** `(21.418s)`.
