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
| Python *with compushady* **(GPU)** | `1.438ms` | `1.429ms` | `1.442ms` | `14.377ms` | 1.00x
| Python *with zengl* **(GPU)** | `5.050ms` | `4.874ms` | `5.434ms` | `50.502ms` | 3.51x
| C# *with ComputeSharp* **(GPU)** | `8.338ms` | `7.923ms` | `10.239ms` | `83.375ms` | 5.80x
| C++ *with no library* **(CPU)** | `8.709ms` | `6.239ms` | `10.851ms` | `87.089ms` | 6.06x
| Zig *with zigimg* **(CPU)** | `30.570ms` | `30.181ms` | `30.866ms` | `305.698ms` | 21.26x
| Rust *with image* **(CPU)** | `67.114ms` | `66.102ms` | `72.121ms` | `671.144ms` | 46.68x
| C# *with ImageSharp* **(CPU)** | `155.268ms` | `152.951ms` | `157.266ms` | `1.553s` | 108.00x
| Go *with image* **(CPU)** | `192.436ms` | `191.498ms` | `193.165ms` | `1.924s` | 133.85x
| Java *with java.awt.image* **(CPU)** | `284.304ms` | `281.878ms` | `285.932ms` | `2.843s` | 197.76x
| Python *with Numba* **(CPU)** | `529.293ms` | `526.011ms` | `533.106ms` | `5.293s` | 368.17x
| Typescript *with node-canvas* **(CPU)** | `1.773s` | `1.764s` | `1.785s` | `17.733s` | 1233.48x
| Python *with Pillow* **(CPU)** | `21.312s` | `20.868s` | `21.662s` | `03:33min` | 14824.52x

---

## Stats

- total time taken: `05:40min`.
- total time taken (just runs): `04:03min`.
- best avg: Python *with compushady* **(GPU)** `(1.438ms)`.
- worst avg: Python *with Pillow* **(CPU)** `(21.312s)`.
