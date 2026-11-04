#!/usr/bin/env python3
import sys
from pipeline_extensions import run_phase_7_rust_transpilation

def main(filepath=None):
    return run_phase_7_rust_transpilation(filepath)

if __name__ == "__main__":
    sys.exit(main())
