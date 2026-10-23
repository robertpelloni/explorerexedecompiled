# TODO

## Immediate Tasks
- [x] Determine the exact target build version of `explorer.exe` to reverse. (Target: Windows 10 Build 19045)
- [x] Set up the basic project structure for C++ output. (Created `src/` and `include/` directories)
- [x] Implement a script to query the Microsoft Symbol Server for PDB retrieval.
- [x] Create a master orchestrator script to link binary ingestion and PDB fetching into a Phase 1 pipeline.
- [x] Phase 2: Containerize a headless disassembler (Ghidra/RetDec) via Docker to run `scripts/decompile.py` consistently.
- [x] Phase 2: Refactor `scripts/decompile.py` to execute headless analysis via Docker and dump Intermediate Representation (IR) / ASTs.
- [x] Phase 3: Develop AST parsing logic to read the dumped C pseudocode from `scripts/DumpC.py` and refine variable naming.
- [x] Phase 3: Develop logic to split the monolithic C pseudocode into logical `src/` modules.
- [x] Phase 3: Implement C++ structural synthesis (header generation) into `include/` based on inferred types from the decompiled logic.
- [x] Phase 4: Implement a build system (CMake/Makefile) to verify the compilability of the reconstructed C++ source code.
- [x] Phase 4: Identify missing OS headers or libraries necessary to resolve `windows.h` and COM objects during the CI verification process.
- [x] Create a master `run_all.sh` orchestrator script to link all phases and provide a single entry point.
- [x] Phase 5: Develop advanced AST parsing (via `libclang` or similar) to structurally flatten `goto` statements rather than simply flagging them via regex.
- [x] Phase 6: Synthesize C++ basic blocks using libclang to rewrite backward `goto` logic into native `while` loops.
- [x] Draft coding guidelines for the generated C++ (naming conventions, documentation rules).
- [x] Wire backend features to a frontend representation (`test_frontend.html`) with interactive forms, clear labels, and descriptions as mandated by Section 5.
- [x] Verify static library linking with C++ sources using CMake.
- [x] Redesign `test_frontend.html` into a high-value consolidated master dashboard with an embedded System Tray Controller, server management controls (Start, Pause, Quit Servers), tooltips, and live telemetry log streaming.
- [x] Reorganize extension scripts into `scripts/pipeline_extensions.py` nondestructively with in-depth comments explaining architectural rationale, structural side effects, and optimizations per Section 5.

## Post-1.0 Objectives
- [x] Create an automated repository synchronization script (`sync.sh`) to fulfill Section 2 upstream merging/submodule cleanup directives.
- [ ] Ingest legitimate `explorer.exe` (Windows 10 Build 19045) using the master pipeline script.
- [x] Resolve any unexpected AST failure cases that emerge from massive production binaries versus the simple mock C++ tests.
