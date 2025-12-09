# Worley Noise Benchmarking
> CPU: AMD Ryzen 7 5700X3D 8-Core Processor (3.00 GHz) |
> GPU: AMD Radeon RX 6600 |
> approx. RAM: 32694 MB |
> approx. VRAM: 8146 MB |
> Width: 1000; Height: 1000; Number of points: 100 |
> 12 programs, 11 runs each (1st run is discarded and not included)

---

## Summary
> sorted by avg

|  Program  |  Average  |  Min  |  Max  |   Total   |  Diff  |
|-----------|:---------:|:-----:|:-----:|:---------:|:------:|
| Python *with compushady* **(GPU)** | `1.322ms` | `1.310ms` | `1.355ms` | `13.216ms` | 1.00x
| Python *with zengl* **(GPU)** | `4.587ms` | `4.512ms` | `4.716ms` | `45.866ms` | 3.47x
| C# *with ComputeSharp* **(GPU)** | `8.146ms` | `7.817ms` | `8.951ms` | `81.457ms` | 6.16x
| C++ *with no library* **(CPU)** | `8.815ms` | `6.240ms` | `18.275ms` | `88.152ms` | 6.67x
| Zig *with zigimg* **(CPU)** | `30.250ms` | `30.127ms` | `30.464ms` | `302.499ms` | 22.89x
| Rust *with image* **(CPU)** | `65.789ms` | `65.454ms` | `66.643ms` | `657.889ms` | 49.78x
| C# *with ImageSharp* **(CPU)** | `154.359ms` | `152.520ms` | `157.735ms` | `1.544s` | 116.79x
| Go *with image* **(CPU)** | `188.937ms` | `188.161ms` | `190.163ms` | `1.889s` | 142.96x
| Java *with java.awt.image* **(CPU)** | `281.845ms` | `279.941ms` | `283.456ms` | `2.818s` | 213.25x
| Python *with Numba* **(CPU)** | `528.330ms` | `524.205ms` | `531.808ms` | `5.283s` | 399.75x
| Typescript *with node-canvas* **(CPU)** | `1.774s` | `1.763s` | `1.783s` | `17.736s` | 1341.95x
| Python *with Pillow* **(CPU)** | `21.449s` | `20.807s` | `22.935s` | `03:34min` | 16228.65x

---

## Stats

- total time taken: `05:52min`.
- total time taken (just runs): `04:04min`.
- best avg: Python *with compushady* **(GPU)** `(1.322ms)`.
- worst avg: Python *with Pillow* **(CPU)** `(21.449s)`.
