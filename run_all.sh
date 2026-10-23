#!/bin/bash
# Master Pipeline Orchestrator for Explorer Decompilation Pipeline
# Handles Phase 0 through Phase 6 core flow, and optional Phase 7-12 extension flows.

set -e

echo "=== Phase 0: Environment Validation ==="
python3 scripts/validate_env.py

if [ -z "$1" ]; then
    echo "Notice: No binary argument passed to ./run_all.sh. Using fallback target or mock environment."
fi

TARGET_BIN="${1:-input/explorer.exe}"

echo "=== Phase 1: PE Ingestion & PDB Symbol Retrieval ==="
python3 scripts/ingest_binary.py "$TARGET_BIN" || true
python3 scripts/fetch_pdb.py || true

echo "=== Phase 2: Headless Ghidra Decompilation ==="
python3 scripts/decompile.py "$TARGET_BIN" || true

echo "=== Phase 3: Pseudocode Refinement & Module Segmentation ==="
python3 scripts/refine_c.py || true
python3 scripts/segment_c.py || true
python3 scripts/synthesize_headers.py || true

echo "=== Phase 4: MinGW-w64 Cross Compilation ==="
mkdir -p build && cd build
cmake .. -DCMAKE_TOOLCHAIN_FILE=../CMakeToolchain-MinGW.cmake || true
make || true
cd ..

echo "=== Phase 5 & 6: AST Control Flow Flattening & Loop Synthesis ==="
python3 scripts/flatten_cfg.py || true
python3 scripts/synthesize_ast_blocks.py || true

if [ "$2" == "--with-extensions" ] || [ "$RUN_EXTENSIONS" == "1" ]; then
    echo "=== Phase 7 - 12: Executing Pipeline Extensions ==="
    python3 scripts/pipeline_extensions.py rust
    python3 scripts/pipeline_extensions.py shell
    python3 scripts/pipeline_extensions.py plugin
    python3 scripts/pipeline_extensions.py graph
    python3 scripts/pipeline_extensions.py vuln
    python3 scripts/pipeline_extensions.py summary
fi

echo "=== Pipeline Execution Complete ==="
