# Worley Noise Benchmarking
> CPU: AMD Ryzen 7 5700X3D 8-Core Processor (3.00 GHz) |
> GPU: AMD Radeon RX 6600 |
> approx. RAM: 32694 MB |
> approx. VRAM: 8146 MB |
> Width: 1000; Height: 1000; Number of points: 100 |
> 12 programs, 11 runs each (1st run is discarded and not included)
> Data gathered on 2025-12-11T04:34:44Z

---

## Summary
> sorted by avg, diffs based on avg

### All Programs
|  Program  |  Average  |  Min  |  Max  |   Total   | Range |  Total Difference  | Relative Difference |
|-----------|:---------:|:-----:|:-----:|:---------:|:------|:------------------:|:-------------------:|
| Python *with compushady* **(GPU)** | `1.319ms` | `1.309ms` | `1.324ms` | `13.190ms` | 15.100µs | - | - |
| Python *with zengl* **(GPU)** | `4.647ms` | `4.531ms` | `4.891ms` | `46.474ms` | 360.100µs | 3.52x | 3.52x |
| C# *with ComputeSharp* **(GPU)** | `8.059ms` | `7.927ms` | `8.194ms` | `80.587ms` | 267.000µs | 6.11x | 1.73x |
| C++ **(CPU)** | `9.060ms` | `6.145ms` | `11.429ms` | `90.602ms` | 5.284ms | 6.87x | 1.12x |
| Zig *with zigimg* **(CPU)** | `30.599ms` | `30.254ms` | `30.954ms` | `305.991ms` | 699.900µs | 23.20x | 3.38x |
| Rust *with image* **(CPU)** | `65.695ms` | `65.485ms` | `66.021ms` | `656.946ms` | 535.700µs | 49.81x | 2.15x |
| Python *with Numba* **(CPU)** | `81.798ms` | `81.653ms` | `82.298ms` | `817.975ms` | 644.700µs | 62.01x | 1.25x |
| C# *with ImageSharp* **(CPU)** | `157.282ms` | `156.099ms` | `158.250ms` | `1.573s` | 2.151ms | 119.24x | 1.92x |
| Go *with image* **(CPU)** | `193.101ms` | `192.550ms` | `194.166ms` | `1.931s` | 1.617ms | 146.40x | 1.23x |
| Java *with java.awt.image* **(CPU)** | `282.149ms` | `280.137ms` | `284.539ms` | `2.821s` | 4.401ms | 213.91x | 1.46x |
| Typescript *with node-canvas* **(CPU)** | `1.805s` | `1.794s` | `1.827s` | `18.052s` | 32.893ms | 1368.58x | 6.40x |
| Python *with Pillow* **(CPU)** | `21.415s` | `21.211s` | `21.835s` | `03:34min` | 623.287ms | 16235.30x | 11.86x |

### CPU Programs
|  Program  |  Average  |  Min  |  Max  |   Total   | Range |  Total Difference  | Relative Difference |
|-----------|:---------:|:-----:|:-----:|:---------:|:------|:------------------:|:-------------------:|
| C++ **(CPU)** | `9.060ms` | `6.145ms` | `11.429ms` | `90.602ms` | 5.284ms | - | - |
| Zig *with zigimg* **(CPU)** | `30.599ms` | `30.254ms` | `30.954ms` | `305.991ms` | 699.900µs | 23.20x | 3.38x |
| Rust *with image* **(CPU)** | `65.695ms` | `65.485ms` | `66.021ms` | `656.946ms` | 535.700µs | 49.81x | 2.15x |
| Python *with Numba* **(CPU)** | `81.798ms` | `81.653ms` | `82.298ms` | `817.975ms` | 644.700µs | 62.01x | 1.25x |
| C# *with ImageSharp* **(CPU)** | `157.282ms` | `156.099ms` | `158.250ms` | `1.573s` | 2.151ms | 119.24x | 1.92x |
| Go *with image* **(CPU)** | `193.101ms` | `192.550ms` | `194.166ms` | `1.931s` | 1.617ms | 146.40x | 1.23x |
| Java *with java.awt.image* **(CPU)** | `282.149ms` | `280.137ms` | `284.539ms` | `2.821s` | 4.401ms | 213.91x | 1.46x |
| Typescript *with node-canvas* **(CPU)** | `1.805s` | `1.794s` | `1.827s` | `18.052s` | 32.893ms | 1368.58x | 6.40x |
| Python *with Pillow* **(CPU)** | `21.415s` | `21.211s` | `21.835s` | `03:34min` | 623.287ms | 16235.30x | 11.86x |

### GPU Programs
|  Program  |  Average  |  Min  |  Max  |   Total   | Range |  Total Difference  | Relative Difference |
|-----------|:---------:|:-----:|:-----:|:---------:|:------|:------------------:|:-------------------:|
| Python *with compushady* **(GPU)** | `1.319ms` | `1.309ms` | `1.324ms` | `13.190ms` | 15.100µs | - | - |
| Python *with zengl* **(GPU)** | `4.647ms` | `4.531ms` | `4.891ms` | `46.474ms` | 360.100µs | 3.52x | 3.52x |
| C# *with ComputeSharp* **(GPU)** | `8.059ms` | `7.927ms` | `8.194ms` | `80.587ms` | 267.000µs | 6.11x | 1.73x |

---

## Stats

- Total time: `06:09min`.
- Sum runtime: `04:00min`.
- Best average time: Python *with compushady* **(GPU)** `(1.319ms)`.
- Worst average time: Python *with Pillow* **(CPU)** `(21.415s)`.
- Largest range: Python *with Pillow* **(CPU)** `(623.287ms)`.
- Smallest range: Python *with compushady* **(GPU)** `(15.100µs)`.
