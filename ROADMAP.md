# ROADMAP

## Phase 1: Exploration & Triage
- [x] Create project scaffolding (Governance docs, memory docs).
- [x] Configure PE extraction (`ingest_binary.py`) and PDB fetching (`fetch_pdb.py`).

## Phase 2: Disassembly & Headless Execution
- [x] Configure headless Java disassembler Docker environment (`Dockerfile`).
- [x] Implement Python orchestrator wrapper (`decompile.py`).
- [x] Implement Java/Jython internal script to rip raw C (`DumpC.py`).

## Phase 3: Initial Reconstruction
- [x] RegEx refinement of variable names and casting (`refine_c.py`).
- [x] Logical segmenting of C files into source and header (`segment_c.py`, `synthesize_headers.py`).

## Phase 4: CI Build Validation
- [x] Configure MinGW-w64 cross compilation and Win32 COM linking (`CMakeLists.txt`, `CMakeToolchain-MinGW.cmake`).

## Phase 5: High Fidelity Restructuring (AST)
- [x] Utilize `libclang` to parse AST and map backward jumping GOTO statements (`flatten_cfg.py`, `synthesize_ast_blocks.py`).

## Phase 6: Orchestration & Frontend UI
- [x] Implement the global Git Sync executive handler (`sync.sh`).
- [x] Implement master `run_all.sh` handler for pipeline Phases 1-6.
- [x] Consolidate master dashboard UI (`test_frontend.html`) with System Tray Controller and daemon process management.

## Phase 7-12: Intelligence, Security & Extensions
- [x] Rust FFI Transpilation (`pipeline_extensions.py` / `transpile_to_rust.py`).
- [x] Kiosk Custom Shell Synthesis (`pipeline_extensions.py` / `generate_custom_shell.py`).
- [x] Modular Plugin Architecture Builder (`pipeline_extensions.py` / `generate_plugin_architecture.py`).
- [x] AST Control Flow Graph Export (`pipeline_extensions.py` / `generate_ast_graph.py`).
- [x] Static Vulnerability Scanner (`pipeline_extensions.py` / `generate_vulnerability_report.py`).
- [x] AI Function Summarizer & Docstring Generator (`pipeline_extensions.py` / `generate_ai_summary.py`).
