# Worley Noise Benchmarking
> CPU: AMD Ryzen 7 5700X3D 8-Core Processor (3.0000 GHz GHz) |
> GPU: AMD Radeon RX 6600 |
> RAM: 32694.5 MB |
> VRAM: 8146 MB |
> Width: 1000; Height: 1000; Number of points: 100 |
> 12 programs, 11 runs each (1st run is discarded and not included)

---

## Summary
> run - total, avg, min and max (sorted by avg)

- Python (GPU, compushady) - `0.014s`, `0.001s`, `0.001s` and `0.001s`.
- Python (GPU, zengl) - `0.051s`, `0.005s`, `0.005s` and `0.006s`.
- C# (GPU, ComputeSharp) - `0.078s`, `0.008s`, `0.007s` and `0.008s`.
- Zig (CPU, zigimg) - `0.302s`, `0.030s`, `0.030s` and `0.031s`.
- Rust (CPU, image) - `0.676s`, `0.068s`, `0.066s` and `0.071s`.
- C++ (CPU, BitmapPlusPlus) - `1.230s`, `0.123s`, `0.121s` and `0.124s`.
- Go (CPU, image) - `1.927s`, `0.193s`, `0.192s` and `0.194s`.
- C# (CPU, ImageSharp) - `2.560s`, `0.256s`, `0.255s` and `0.258s`.
- Java (CPU, java.awt.image) - `3.659s`, `0.366s`, `0.360s` and `0.381s`.
- Python (CPU, Numba) - `5.409s`, `0.541s`, `0.535s` and `0.546s`.
- Typescript (CPU, node-canvas) - `18.386s`, `1.839s`, `1.808s` and `1.864s`.
- Python (CPU, Pillow) - `03:34min`, `21.434s`, `21.261s` and `21.626s`.

---

## All runs
> run - timings (sorted by avg)

- Python (GPU, compushady) - `0.001s`, `0.001s`, `0.001s`, `0.001s`, `0.001s`, `0.001s`, `0.001s`, `0.001s`, `0.001s` and `0.001s`.
- Python (GPU, zengl) - `0.005s`, `0.005s`, `0.005s`, `0.005s`, `0.005s`, `0.005s`, `0.006s`, `0.005s`, `0.005s` and `0.005s`.
- C# (GPU, ComputeSharp) - `0.008s`, `0.008s`, `0.008s`, `0.008s`, `0.008s`, `0.008s`, `0.008s`, `0.008s`, `0.007s` and `0.007s`.
- Zig (CPU, zigimg) - `0.031s`, `0.030s`, `0.030s`, `0.030s`, `0.031s`, `0.030s`, `0.030s`, `0.031s`, `0.030s` and `0.030s`.
- Rust (CPU, image) - `0.066s`, `0.068s`, `0.068s`, `0.066s`, `0.071s`, `0.069s`, `0.067s`, `0.066s`, `0.067s` and `0.067s`.
- C++ (CPU, BitmapPlusPlus) - `0.124s`, `0.122s`, `0.124s`, `0.122s`, `0.123s`, `0.124s`, `0.123s`, `0.121s`, `0.123s` and `0.124s`.
- Go (CPU, image) - `0.193s`, `0.193s`, `0.192s`, `0.194s`, `0.193s`, `0.193s`, `0.193s`, `0.193s`, `0.192s` and `0.193s`.
- C# (CPU, ImageSharp) - `0.257s`, `0.255s`, `0.255s`, `0.255s`, `0.258s`, `0.256s`, `0.255s`, `0.255s`, `0.257s` and `0.257s`.
- Java (CPU, java.awt.image) - `0.363s`, `0.360s`, `0.364s`, `0.362s`, `0.381s`, `0.365s`, `0.377s`, `0.361s`, `0.364s` and `0.361s`.
- Python (CPU, Numba) - `0.546s`, `0.541s`, `0.545s`, `0.538s`, `0.541s`, `0.542s`, `0.536s`, `0.539s`, `0.546s` and `0.535s`.
- Typescript (CPU, node-canvas) - `1.843s`, `1.864s`, `1.853s`, `1.834s`, `1.834s`, `1.843s`, `1.848s`, `1.826s`, `1.808s` and `1.833s`.
- Python (CPU, Pillow) - `21.378s`, `21.358s`, `21.445s`, `21.440s`, `21.422s`, `21.391s`, `21.559s`, `21.626s`, `21.261s` and `21.463s`.

---

## Stats

- best avg: `Python (GPU, compushady)`.
- worst avg: `Python (CPU, Pillow)`.
- total time taken (just runs): `04:8min`.
- total time taken (including prep): `05:39min`.
