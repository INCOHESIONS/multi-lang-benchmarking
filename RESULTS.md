# Worley Noise Benchmarking
> CPU: AMD Ryzen 7 5700X3D 8-Core Processor (3.00 GHz) |
> GPU: AMD Radeon RX 6600 |
> approx. RAM: 32694 MB |
> approx. VRAM: 8146 MB |
> Width: 1000; Height: 1000; Number of points: 100 |
> 12 programs, 11 runs each (1st run is discarded and not included) |
> Data gathered on 2025-12-11T05:13:37Z

---

## Summary
> sorted by avg, diffs based on avg

### All Programs
|  Program  |  Average  |  Min  |  Max  |   Total   | Range |  Total Difference  | Relative Difference |
|-----------|:---------:|:-----:|:-----:|:---------:|:------|:------------------:|:-------------------:|
| Python *with compushady* **(GPU)** | `1.346ms` | `1.339ms` | `1.369ms` | `13.458ms` | `29.600µs` | - | - |
| Python *with zengl* **(GPU)** | `4.927ms` | `4.760ms` | `5.198ms` | `49.266ms` | `438.400µs` | `3.66x` | `3.66x` |
| C# *with ComputeSharp* **(GPU)** | `8.100ms` | `7.936ms` | `8.249ms` | `80.997ms` | `313.300µs` | `6.02x` | `1.64x` |
| C++ **(CPU)** | `11.287ms` | `6.145ms` | `28.955ms` | `112.872ms` | `22.810ms` | `8.39x` | `1.39x` |
| Zig *with zigimg* **(CPU)** | `30.775ms` | `30.288ms` | `31.252ms` | `307.747ms` | `963.200µs` | `22.87x` | `2.73x` |
| Rust *with image* **(CPU)** | `65.830ms` | `65.553ms` | `66.263ms` | `658.298ms` | `710.500µs` | `48.92x` | `2.14x` |
| Python *with Numba* **(CPU)** | `81.681ms` | `81.641ms` | `81.840ms` | `816.814ms` | `198.700µs` | `60.69x` | `1.24x` |
| C# *with ImageSharp* **(CPU)** | `154.542ms` | `152.375ms` | `157.193ms` | `1.545s` | `4.818ms` | `114.83x` | `1.89x` |
| Go *with image* **(CPU)** | `192.593ms` | `191.556ms` | `193.666ms` | `1.926s` | `2.110ms` | `143.11x` | `1.25x` |
| Java *with java.awt.image* **(CPU)** | `283.792ms` | `280.647ms` | `288.587ms` | `2.838s` | `7.940ms` | `210.88x` | `1.47x` |
| Typescript *with node-canvas* **(CPU)** | `1.803s` | `1.790s` | `1.820s` | `18.029s` | `29.311ms` | `1339.67x` | `6.35x` |
| Python *with Pillow* **(CPU)** | `21.493s` | `21.338s` | `21.675s` | `03:34min` | `337.414ms` | `15970.33x` | `11.92x` |

### CPU Programs
|  Program  |  Average  |  Min  |  Max  |   Total   | Range |  Total Difference  | Relative Difference |
|-----------|:---------:|:-----:|:-----:|:---------:|:------|:------------------:|:-------------------:|
| C++ **(CPU)** | `11.287ms` | `6.145ms` | `28.955ms` | `112.872ms` | `22.810ms` | - | - |
| Zig *with zigimg* **(CPU)** | `30.775ms` | `30.288ms` | `31.252ms` | `307.747ms` | `963.200µs` | `22.87x` | `2.73x` |
| Rust *with image* **(CPU)** | `65.830ms` | `65.553ms` | `66.263ms` | `658.298ms` | `710.500µs` | `48.92x` | `2.14x` |
| Python *with Numba* **(CPU)** | `81.681ms` | `81.641ms` | `81.840ms` | `816.814ms` | `198.700µs` | `60.69x` | `1.24x` |
| C# *with ImageSharp* **(CPU)** | `154.542ms` | `152.375ms` | `157.193ms` | `1.545s` | `4.818ms` | `114.83x` | `1.89x` |
| Go *with image* **(CPU)** | `192.593ms` | `191.556ms` | `193.666ms` | `1.926s` | `2.110ms` | `143.11x` | `1.25x` |
| Java *with java.awt.image* **(CPU)** | `283.792ms` | `280.647ms` | `288.587ms` | `2.838s` | `7.940ms` | `210.88x` | `1.47x` |
| Typescript *with node-canvas* **(CPU)** | `1.803s` | `1.790s` | `1.820s` | `18.029s` | `29.311ms` | `1339.67x` | `6.35x` |
| Python *with Pillow* **(CPU)** | `21.493s` | `21.338s` | `21.675s` | `03:34min` | `337.414ms` | `15970.33x` | `11.92x` |

### GPU Programs
|  Program  |  Average  |  Min  |  Max  |   Total   | Range |  Total Difference  | Relative Difference |
|-----------|:---------:|:-----:|:-----:|:---------:|:------|:------------------:|:-------------------:|
| Python *with compushady* **(GPU)** | `1.346ms` | `1.339ms` | `1.369ms` | `13.458ms` | `29.600µs` | - | - |
| Python *with zengl* **(GPU)** | `4.927ms` | `4.760ms` | `5.198ms` | `49.266ms` | `438.400µs` | `3.66x` | `3.66x` |
| C# *with ComputeSharp* **(GPU)** | `8.100ms` | `7.936ms` | `8.249ms` | `80.997ms` | `313.300µs` | `6.02x` | `1.64x` |

---

## Stats

- Total time: `05:42min`.
- Sum runtime: `04:01min`.
- Best average time: Python *with compushady* **(GPU)** `(1.346ms)`.
- Worst average time: Python *with Pillow* **(CPU)** `(21.493s)`.
- Largest range: Python *with Pillow* **(CPU)** `(337.414ms)`.
- Smallest range: Python *with compushady* **(GPU)** `(29.600µs)`.
