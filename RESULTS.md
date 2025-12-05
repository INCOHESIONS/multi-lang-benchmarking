# Worley Noise Benchmarking
> CPU: AMD Ryzen 7 5700X3D 8-Core Processor |
> GPU: AMD Radeon RX 6600 |
> RAM: 32694.5 MB |
> VRAM: 8146 MB |
> Width: 1000; Height: 1000; Number of points: 100 |
> 10 directories, 11 runs each (1st run is discarded and not included)

------------------------------------------------------------------------------

## Summary
> run - total, avg, min and max

- C# (CPU, ImageSharp) - `4.282s`, `0.428s`, `0.424s` and `0.442s`.
- C# (GPU, ComputeSharp) - `0.077s`, `0.008s`, `0.007s` and `0.008s`.
- C++ (CPU, BitmapPlusPlus) - `7.278s`, `0.728s`, `0.722s` and `0.731s`.
- Go (CPU, image) - `12.744s`, `1.274s`, `1.270s` and `1.279s`.
- Java (CPU, java.awt.image) - `9.868s`, `0.987s`, `0.974s` and `0.996s`.
- Python (CPU, Pillow) - `4.585min`, `27.510s`, `27.299s` and `27.808s`.
- Python (GPU, compushady) - `0.010s`, `0.001s`, `0.001s` and `0.001s`.
- Python (GPU, zengl) - `0.052s`, `0.005s`, `0.005s` and `0.005s`.
- Rust (CPU, image) - `7.928s`, `0.793s`, `0.790s` and `0.800s`.
- Typescript (CPU, node-canvas) - `53.280s`, `5.328s`, `5.297s` and `5.377s`.

------------------------------------------------------------------------------

## All runs
> run - timings

- C# (CPU, ImageSharp) - `0.424s`, `0.424s`, `0.442s`, `0.426s`, `0.426s`, `0.424s`, `0.433s`, `0.426s`, `0.424s` and `0.433s`.
- C# (GPU, ComputeSharp) - `0.007s`, `0.008s`, `0.008s`, `0.007s`, `0.008s`, `0.008s`, `0.007s`, `0.008s`, `0.008s` and `0.008s`.
- C++ (CPU, BitmapPlusPlus) - `0.722s`, `0.723s`, `0.731s`, `0.724s`, `0.731s`, `0.729s`, `0.731s`, `0.731s`, `0.731s` and `0.726s`.
- Go (CPU, image) - `1.273s`, `1.271s`, `1.270s`, `1.277s`, `1.275s`, `1.277s`, `1.279s`, `1.276s`, `1.271s` and `1.276s`.
- Java (CPU, java.awt.image) - `0.980s`, `0.996s`, `0.979s`, `0.995s`, `0.987s`, `0.982s`, `0.974s`, `0.996s`, `0.987s` and `0.992s`.
- Python (CPU, Pillow) - `27.299s`, `27.453s`, `27.542s`, `27.520s`, `27.477s`, `27.511s`, `27.752s`, `27.321s`, `27.808s` and `27.419s`.
- Python (GPU, compushady) - `0.001s`, `0.001s`, `0.001s`, `0.001s`, `0.001s`, `0.001s`, `0.001s`, `0.001s`, `0.001s` and `0.001s`.
- Python (GPU, zengl) - `0.005s`, `0.005s`, `0.005s`, `0.005s`, `0.005s`, `0.005s`, `0.005s`, `0.005s`, `0.005s` and `0.005s`.
- Rust (CPU, image) - `0.790s`, `0.790s`, `0.791s`, `0.793s`, `0.790s`, `0.794s`, `0.796s`, `0.792s`, `0.792s` and `0.800s`.
- Typescript (CPU, node-canvas) - `5.333s`, `5.340s`, `5.305s`, `5.298s`, `5.335s`, `5.377s`, `5.348s`, `5.335s`, `5.312s` and `5.297s`.

------------------------------------------------------------------------------

## Stats

- best avg: `Python (GPU, compushady)`.
- worst avg: `Python (CPU, Pillow)`.
- total time taken (just runs): `6.177min`.
- total time taken (including prep): `7.735min`.

------------------------------------------------------------------------------
