# Worley Noise Benchmarking
> CPU: AMD Ryzen 7 5700X3D 8-Core Processor (3.00 GHz) |
> GPU: AMD Radeon RX 6600 |
> RAM: 32694.5 MB |
> VRAM: 8146 MB |
> Width: 1000; Height: 1000; Number of points: 100 |
> 12 programs, 11 runs each (1st run is discarded and not included)

---

## Summary
> run - total, avg, min and max (sorted by avg)

- Python (GPU, compushady) - `0.014s`, `0.001s`, `0.001s` and `0.001s`.
- Python (GPU, zengl) - `0.054s`, `0.005s`, `0.005s` and `0.006s`.
- C# (GPU, ComputeSharp) - `0.080s`, `0.008s`, `0.007s` and `0.009s`.
- C++ (CPU, BitmapPlusPlus) - `0.118s`, `0.012s`, `0.010s` and `0.017s`.
- Zig (CPU, zigimg) - `0.302s`, `0.030s`, `0.030s` and `0.031s`.
- Rust (CPU, image) - `0.688s`, `0.069s`, `0.067s` and `0.073s`.
- C# (CPU, ImageSharp) - `2.548s`, `0.255s`, `0.254s` and `0.257s`.
- Go (CPU, image) - `2.870s`, `0.287s`, `0.244s` and `0.311s`.
- Python (CPU, Numba) - `5.307s`, `0.531s`, `0.523s` and `0.547s`.
- Java (CPU, java.awt.image) - `5.574s`, `0.557s`, `0.412s` and `0.596s`.
- Typescript (CPU, node-canvas) - `19.423s`, `1.942s`, `1.831s` and `2.103s`.
- Python (CPU, Pillow) - `03:38min`, `21.868s`, `20.768s` and `25.377s`.

---

## All runs
> run - timings (sorted by avg)

- Python (GPU, compushady) - `0.001s`, `0.001s`, `0.001s`, `0.001s`, `0.001s`, `0.001s`, `0.001s`, `0.001s`, `0.001s` and `0.001s`.
- Python (GPU, zengl) - `0.006s`, `0.005s`, `0.006s`, `0.005s`, `0.005s`, `0.005s`, `0.005s`, `0.005s`, `0.006s` and `0.005s`.
- C# (GPU, ComputeSharp) - `0.007s`, `0.008s`, `0.009s`, `0.008s`, `0.008s`, `0.008s`, `0.008s`, `0.008s`, `0.008s` and `0.008s`.
- C++ (CPU, BitmapPlusPlus) - `0.011s`, `0.010s`, `0.012s`, `0.017s`, `0.016s`, `0.011s`, `0.010s`, `0.010s`, `0.013s` and `0.010s`.
- Zig (CPU, zigimg) - `0.030s`, `0.030s`, `0.031s`, `0.030s`, `0.031s`, `0.031s`, `0.030s`, `0.030s`, `0.030s` and `0.031s`.
- Rust (CPU, image) - `0.073s`, `0.068s`, `0.068s`, `0.067s`, `0.067s`, `0.069s`, `0.069s`, `0.068s`, `0.073s` and `0.067s`.
- C# (CPU, ImageSharp) - `0.254s`, `0.257s`, `0.255s`, `0.254s`, `0.255s`, `0.255s`, `0.255s`, `0.254s`, `0.255s` and `0.254s`.
- Go (CPU, image) - `0.301s`, `0.300s`, `0.309s`, `0.306s`, `0.311s`, `0.306s`, `0.292s`, `0.252s`, `0.248s` and `0.244s`.
- Python (CPU, Numba) - `0.547s`, `0.540s`, `0.527s`, `0.528s`, `0.526s`, `0.526s`, `0.531s`, `0.524s`, `0.523s` and `0.534s`.
- Java (CPU, java.awt.image) - `0.596s`, `0.585s`, `0.587s`, `0.568s`, `0.560s`, `0.596s`, `0.590s`, `0.587s`, `0.493s` and `0.412s`.
- Typescript (CPU, node-canvas) - `2.103s`, `1.971s`, `1.919s`, `2.054s`, `2.043s`, `1.907s`, `1.877s`, `1.831s`, `1.867s` and `1.850s`.
- Python (CPU, Pillow) - `20.768s`, `21.072s`, `21.517s`, `20.877s`, `25.377s`, `21.480s`, `21.288s`, `21.168s`, `21.646s` and `23.490s`.

---

## Stats

- best avg: `Python (GPU, compushady)`.
- worst avg: `Python (CPU, Pillow)`.
- total time taken (just runs): `04:15min`.
- total time taken (including prep): `06:22min`.
