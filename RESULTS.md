# Worley Noise Benchmarking
> CPU: AMD Ryzen 7 5700X3D 8-Core Processor (3.00 GHz) |
> GPU: AMD Radeon RX 6600 |
> approx. RAM: 32694 MB |
> approx. VRAM: 8146 MB |
> Width: 1000; Height: 1000; Number of points: 100 |
> 12 programs, 11 runs each (1st run is discarded and not included) |
> Data gathered on 2025-12-11T15:00:47Z

---

## Summary
> sorted by avg, diffs based on avg

### All Programs
|  Program  |  Average  |  Min  |  Max  |   Total   | Range  |  Total Difference  | Relative Difference |
|-----------|:---------:|:-----:|:-----:|:---------:|:------:|:------------------:|:-------------------:|
| Python *with compushady* **(GPU)** | `1.345ms` | `1.341ms` | `1.349ms` | `13.448ms` | `7.400µs` | - | - |
| Python *with zengl* **(GPU)** | `5.359ms` | `4.874ms` | `8.252ms` | `53.593ms` | `3.378ms` | `3.99x` | `3.99x` |
| C# *with ComputeSharp* **(GPU)** | `8.163ms` | `8.024ms` | `8.327ms` | `81.629ms` | `302.600µs` | `6.07x` | `1.52x` |
| C++ **(CPU)** | `8.910ms` | `6.263ms` | `14.412ms` | `89.101ms` | `8.149ms` | `6.63x` | `1.09x` |
| Zig *with zigimg* **(CPU)** | `30.640ms` | `30.239ms` | `30.932ms` | `306.398ms` | `692.600µs` | `22.78x` | `3.44x` |
| Rust *with image* **(CPU)** | `65.994ms` | `65.562ms` | `66.826ms` | `659.938ms` | `1.264ms` | `49.07x` | `2.15x` |
| Python *with Numba* **(CPU)** | `81.993ms` | `81.658ms` | `82.673ms` | `819.932ms` | `1.015ms` | `60.97x` | `1.24x` |
| C# *with ImageSharp* **(CPU)** | `157.731ms` | `154.364ms` | `163.747ms` | `1.577s` | `9.383ms` | `117.29x` | `1.92x` |
| Go *with image* **(CPU)** | `193.066ms` | `192.164ms` | `193.667ms` | `1.931s` | `1.503ms` | `143.57x` | `1.22x` |
| Java *with java.awt.image* **(CPU)** | `284.235ms` | `281.803ms` | `293.130ms` | `2.842s` | `11.327ms` | `211.36x` | `1.47x` |
| Typescript *with node-canvas* **(CPU)** | `1.920s` | `1.900s` | `1.943s` | `19.199s` | `42.433ms` | `1427.71x` | `6.75x` |
| Python *with Pillow* **(CPU)** | `21.739s` | `21.300s` | `22.967s` | `03:37min` | `1.668s` | `16165.53x` | `11.32x` |

### CPU Programs
|  Program  |  Average  |  Min  |  Max  |   Total   | Range  |  Total Difference  | Relative Difference |
|-----------|:---------:|:-----:|:-----:|:---------:|:------:|:------------------:|:-------------------:|
| C++ **(CPU)** | `8.910ms` | `6.263ms` | `14.412ms` | `89.101ms` | `8.149ms` | - | - |
| Zig *with zigimg* **(CPU)** | `30.640ms` | `30.239ms` | `30.932ms` | `306.398ms` | `692.600µs` | `3.44x` | `3.44x` |
| Rust *with image* **(CPU)** | `65.994ms` | `65.562ms` | `66.826ms` | `659.938ms` | `1.264ms` | `7.41x` | `2.15x` |
| Python *with Numba* **(CPU)** | `81.993ms` | `81.658ms` | `82.673ms` | `819.932ms` | `1.015ms` | `9.20x` | `1.24x` |
| C# *with ImageSharp* **(CPU)** | `157.731ms` | `154.364ms` | `163.747ms` | `1.577s` | `9.383ms` | `17.70x` | `1.92x` |
| Go *with image* **(CPU)** | `193.066ms` | `192.164ms` | `193.667ms` | `1.931s` | `1.503ms` | `21.67x` | `1.22x` |
| Java *with java.awt.image* **(CPU)** | `284.235ms` | `281.803ms` | `293.130ms` | `2.842s` | `11.327ms` | `31.90x` | `1.47x` |
| Typescript *with node-canvas* **(CPU)** | `1.920s` | `1.900s` | `1.943s` | `19.199s` | `42.433ms` | `215.48x` | `6.75x` |
| Python *with Pillow* **(CPU)** | `21.739s` | `21.300s` | `22.967s` | `03:37min` | `1.668s` | `2439.81x` | `11.32x` |

### GPU Programs
|  Program  |  Average  |  Min  |  Max  |   Total   | Range  |  Total Difference  | Relative Difference |
|-----------|:---------:|:-----:|:-----:|:---------:|:------:|:------------------:|:-------------------:|
| Python *with compushady* **(GPU)** | `1.345ms` | `1.341ms` | `1.349ms` | `13.448ms` | `7.400µs` | - | - |
| Python *with zengl* **(GPU)** | `5.359ms` | `4.874ms` | `8.252ms` | `53.593ms` | `3.378ms` | `3.99x` | `3.99x` |
| C# *with ComputeSharp* **(GPU)** | `8.163ms` | `8.024ms` | `8.327ms` | `81.629ms` | `302.600µs` | `6.07x` | `1.52x` |

---

## Stats

- Total time: `06:14min`.
- Sum runtime: `04:04min`.
- Best average time: Python *with compushady* **(GPU)** `(1.345ms)`.
- Worst average time: Python *with Pillow* **(CPU)** `(21.739s)`.
- Largest range: Python *with Pillow* **(CPU)** `(1.668s)`.
- Smallest range: Python *with compushady* **(GPU)** `(7.400µs)`.
