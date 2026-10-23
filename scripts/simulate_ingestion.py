#!/usr/bin/env python3
import os
import shutil
import subprocess
import sys

def get_compiler():
    compilers = ['x86_64-w64-mingw32-gcc', 'gcc', 'clang', 'cc']
    for c in compilers:
        if shutil.which(c):
            return c
    return None

def main():
    print("=== EXPLORER.EXE INGESTION SIMULATOR ===")
    print("Simulating human maintainer providing the proprietary binary...")

    compiler = get_compiler()
    if not compiler:
        print("ERROR: No suitable C compiler found in PATH.")
        return 1

    input_dir = "input"
    target_exe = os.path.join(input_dir, "explorer.exe")
    dummy_c = "simulate_dummy.c"

    os.makedirs(input_dir, exist_ok=True)

    # Synthesize the placeholder PE
    with open(dummy_c, "w") as f:
        f.write("int main() { return 0; }\n")

    print(f"Compiling minimal placeholder binary using {compiler} to {target_exe}...")
    compile_cmd = [compiler, dummy_c, "-o", target_exe]

    try:
        subprocess.run(compile_cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        print(f"Compilation failed: {e.stderr.decode()}")
        if os.path.exists(dummy_c): os.remove(dummy_c)
        return 1

    # Clean up dummy C file
    if os.path.exists(dummy_c):
        os.remove(dummy_c)

    print(f"Placeholder created. Triggering master pipeline: ./run_all.sh {target_exe}\n")
    print("-" * 50)

    # Execute the master orchestrator
    try:
        process = subprocess.Popen(["./run_all.sh", target_exe], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        for line in process.stdout:
            print(line, end="")
        process.wait()

        if process.returncode != 0:
            print(f"\nPipeline execution returned non-zero exit code: {process.returncode}")
            return process.returncode

    except FileNotFoundError:
        print("\nERROR: ./run_all.sh not found. Ensure you are running this from the repository root.")
        return 1

    print("-" * 50)
    print("\nSimulation complete. The end-to-end pipeline wrapper has successfully functioned.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
