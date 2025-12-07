clang .\main.cpp -std=c++23 -march=native -O3 -fomit-frame-pointer -funroll-loops -ffast-math -fno-trapping-math -fno-signed-zeros -freciprocal-math -fopenmp -fuse-ld=lld -flto -o program.exe
