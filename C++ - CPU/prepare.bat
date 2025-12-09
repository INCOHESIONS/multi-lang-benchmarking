clang .\main.cpp -std=c++23 -march=native -O3 -fomit-frame-pointer -funroll-loops -funsafe-math-optimizations -fopenmp -fuse-ld=lld -flto -o program.exe
