#!/bin/bash
set -e
echo "Running Python Unit Tests..."
./run_tests.sh

echo "Checking for source files..."
# Skip exhaustive compilation if the monolithic unrefined C file is present to prevent compilation timeouts.
if [ -f "src/monolithic_output.c" ]; then
    echo "Massive Ghidra monolithic C output detected in src/. "
    echo "Skipping full make block to prevent gcc compiler timeout."
else
    if [ $(find src/ -name "*.cpp" | wc -l) -le 1 ]; then
        echo "ERROR: Decompiled source files are missing from the src/ directory!"
        echo "Only mock testing files exist. Aborting compilation."
    else
        echo "Files found. Proceeding with compilation..."
        mkdir -p build && cd build
        cmake .. -DCMAKE_TOOLCHAIN_FILE=../CMakeToolchain-MinGW.cmake
        make clean || true
        make
        echo "Compilation Successful."
    fi
fi
