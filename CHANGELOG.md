# CHANGELOG

## [1.2.33] - Phase 3 C Refinement & Header Synthesis Enhancements
- Enhanced `scripts/refine_c.py` to perform macro cleanup, Ghidra primitive type normalization (`undefined4` -> `uint32_t`, `undefined8` -> `uint64_t`), and automatic stdint header injection.
- Enhanced `scripts/segment_c.py` and `scripts/synthesize_headers.py` to parse function declarations and emit modular C++ source files (`src/module_0.cpp`) and header prototypes (`include/module_0.h`).
- Added in-depth architectural comments across Phase 3 scripts detailing why, structural side effects, discovered optimizations, and attempted alternatives per Section 5 instructions.
- Expanded `scripts/test_pipeline_mocks.py` unit test coverage to 15 passing tests.

## [1.2.32] - UI Redesign, System Tray Integration & Script Reorganization
- Redesigned `test_frontend.html` into a consolidated single-page dashboard categorized by high value (Core Decompilation Engine, Intelligence & Security Diagnostics, Advanced Architecture Generators).
- Added an interactive System Tray Icon widget and controller to `test_frontend.html` with functional daemon start, pause, clear logs, and server quit capabilities.
- Added tooltip markers (`[?]`) and descriptive guidance across all dashboard fields, phase cards, and system controls.
- Reorganized and refactored pipeline extension scripts into `scripts/pipeline_extensions.py` with in-depth comments explaining architectural rationale, structural side effects, and optimizations per Section 5 directives.
- Archiving original extension helpers into `scripts/archive/` while retaining thin, backward-compatible shims for CLI and unittest compatibility.
- Updated `run_all.sh` to support optional extension execution passes (`--with-extensions`).
- Validated UI updates via Playwright in `scripts/verify_frontend.py` and captured screenshot artifacts in `verification/screenshots/verification.png`.

## [1.2.31] - Programmatic Loop Synthesis
- Refactored `scripts/synthesize_ast_blocks.py` to identify backwards `GOTO_STMT` tokens relative to their `LABEL_STMT` targets via libclang.
- Programmatically overwrites identified backwards gotos inside the authentic C target files into safe `while(true)` blocks using AST index mapping, fundamentally transitioning the pipeline to a true code structural rewriting framework.

## [1.2.30] - AST Control Flow Processing
- Implemented core AST processing hooks in `scripts/flatten_cfg.py` and `scripts/synthesize_ast_blocks.py` using `libclang` to parse and flag `GOTO_STMT` and `LABEL_STMT` tokens within the native Ghidra output.

## [1.2.29] - AST Evaluation Profiler
- Added `scripts/evaluate_parsers.py` to test the limits of `libclang` when building massive syntax trees directly from Ghidra pseudo-C output.

## [1.2.28] - Phase 4 Mock Visualization
- Added inline warnings to `test_frontend.html` during the Phase 4 Cross Compilation cycle to actively indicate to end-users that the `explorer.exe` C++ source is utilizing the mock fallback mechanism rather than exhaustive raw Ghidra building.

## [1.2.26] - Real Ghidra Headless Integration
- Configured the `Dockerfile` to successfully download and install a real, non-mock distribution of Ghidra (11.0.3) to power Phase 2.
- Removed the mock `analyzeHeadless` bash script and replaced `scripts/DumpC.py` with a functional Jython decompilation script that natively interacts with Ghidra's `DecompInterface`.
- Validated real execution of `run_all.sh` Phase 2, which now successfully yields a complete 7.0MB C pseudocode file (`monolithic_output.c`) representing the decompiled `explorer.exe` executable!
- Fixed `.gitignore` to ensure `project/` workspace locks and the massive generated C files do not blow up version control.

## [1.2.25] - Native Ghidra Docker Environment Initialization
- Fixed Docker overlayfs bugs in the local workspace by modifying the daemon `storage-driver` to `vfs`.
- Successfully built the `ghidra-decompiler` Docker image natively to run Phase 2 containerized decompilation workflows.
- Evaluated `scripts/decompile.py` locally against the active `explorer.exe` binary.

## [1.2.23] - AI Code Summarization Mock & UI Redesign Integration
- Expanded `IDEAS.md` to include AI Code Summarization.
- Implemented `scripts/generate_ai_summary.py` to simulate a new "Phase 12: AI Code Summarization" feature.
- Added unit tests for the new script in `scripts/test_pipeline_mocks.py`.
- Substantially redesigned `test_frontend.html` per user requirements to condense all functionality onto a single dashboard page.
- Grouped phases logically into Core Pipeline, Verification/Debugging, and Experimental Expansions.
- Validated frontend UI updates visually using Playwright script `scripts/verify_frontend.py` to ensure visual artifacts are correct.

## [1.2.21] - Vulnerability Scanner Mock & UI Integration
- Expanded `IDEAS.md` to include Automated Vulnerability Scanning.
- Implemented `scripts/generate_vulnerability_report.py` to simulate a new "Phase 11: Automated Vulnerability Scanning" feature.
- Added unit tests for the new script in `scripts/test_pipeline_mocks.py`.
- Updated `test_frontend.html` dashboard UI to include an interactive toggle for Phase 11.
- Validated frontend UI updates visually using Playwright script `scripts/verify_frontend.py` to ensure visual artifacts are correct.

## [1.2.20] - AST Graph Visualization Mock & Flattener Polish
- Refined `scripts/flatten_cfg.py` by implementing a recursive AST traversal function `recursive_flatten` to find explicitly declared GOTOs and labels to prepare for restructuring into basic blocks.
- Implemented `scripts/generate_ast_graph.py` to simulate a new "Phase 10: AST Graph Visualization" debugging feature.
- Added unit tests for the new script in `scripts/test_pipeline_mocks.py`.
- Updated `test_frontend.html` dashboard UI to include an interactive toggle for Phase 10.
- Validated frontend UI updates visually using Playwright script `scripts/verify_frontend.py` to ensure visual artifacts are correct.

## [1.2.19] - Plugin Architecture Mock & UI Integration
- Implemented `scripts/generate_plugin_architecture.py` to simulate the Phase 9 "Plugin Architecture" feature from `IDEAS.md`.
- Added unit tests for the new script in `scripts/test_pipeline_mocks.py`.
- Updated `test_frontend.html` dashboard UI to include an interactive toggle for Phase 9.
- Validated frontend UI updates visually using Playwright script `scripts/verify_frontend.py` to ensure visual artifacts are correct.

## [1.2.18] - Custom Shell Variation Mock & UI Integration
- Implemented `scripts/generate_custom_shell.py` to simulate the Phase 8 "Generate Custom Shell" feature from `IDEAS.md`.
- Added unit tests for the new script in `scripts/test_pipeline_mocks.py`.
- Updated `test_frontend.html` dashboard UI to include an interactive toggle for Phase 8.
- Validated frontend UI updates visually using Playwright script `scripts/verify_frontend.py` to ensure visual artifacts are correct.

## [1.2.16] - UI Feature Parity & Rust Transpilation Mocking
- Executed an audit of IDEAS.md and implemented a mock Python script (`scripts/transpile_to_rust.py`) to simulate translating the extracted C AST into unsafe Rust FFI bindings.
- Added a comprehensive testing suite for this transpilation script into `test_pipeline_mocks.py`.
- Formally mapped this new experimental "Phase 7" into the UI via `test_frontend.html`.
- Implemented interactive checkboxes, descriptive tooltips, and dynamic logic to stream the Rust generation logs to the simulated UI console if selected.
- Verified UI updates rigorously via Playwright (`sync_playwright`), confirming all visual states.

## [1.2.15] - Placeholder Execution, Validation, and Tooling Edge Cases
- Synthesized minimal placeholder PE target using MinGW-w64 to robustly test the pipeline's ingestion and parsing validation logic without requiring physical binary drops.
- Drafted mock capabilities for logic segmentation (`segment_c.py`) and AST basic block synthesis (`synthesize_ast_blocks.py`).
- Added edge case unittests in `test_pipeline_mocks.py` to assert AST recursion handling (deeply nested GOTOs) and grace degradation on malformed C structs.
- Implemented fully automated CI/CD workflow testing for PRs and main branches targeting Ubuntu-22.04 with GCC toolchains inside `.github/workflows/ci.yml`.
- Configured local environment validation checkpoints (`validate_env.py`) checking dependencies (`pefile`, `cmake`, `clang`, etc.) actively enforcing Section 2 prep procedures.
- Delivered frontend UI orchestration matching Section 5 dictates dynamically streaming pipeline phase states to simulated consoles via `test_frontend.html`.
- Defined expectations internally on expected PDB boundaries targeting Windows Build 19045 explicit artifacts within `BINARY_INTERFACE.md`.

## [1.2.8] - Resynchronization Execution
- Triggered automated `sync.sh` resolution to pull upstream changes and manage stash workflows per updated protocols. No compilation action taken due to missing source files.

## [1.2.7] - Documentation Polish
- Explicitly documented cross-compilation execution block within `README.md` to guide future developers attempting to manually rebuild the missing `explorer.exe` C++ sources on Linux using CMake/MinGW.

## [1.2.6] - Compilation Pipeline Hardening
- Added an initial C++ mock class to `src/test_main.cpp`.
- Validated that `CMakeLists.txt` builds the `.a` library successfully out of `src/` correctly applying the toolchain configurations.

## [1.2.5] - Frontend & Architecture Verification
- Implemented `test_frontend.html` satisfying Section 5 UI directives to expose the backend pipeline visually.

## [1.2.4] - Robustified Automation Integration
- Improved `ingest_binary.py` to actually extract the CodeView Debug directory and dump `pdb_info.txt`.
- Improved `fetch_pdb.py` to read `pdb_info.txt` and invoke `urllib` to hit the Microsoft Symbol server.
- Fixed `run_all.sh` to correctly pass the binary argument to Phase 2 scripts.
- Fixed `CMakeLists.txt` linker language missing issues when Ghidra dumps raw C instead of C++.

## [1.2.3] - Scaffolded Automation Pipeline
- Implemented Phase 1 PE/PDB Ingestion logic.
- Implemented Phase 2 Headless Docker Decompilation logic.
- Implemented Phase 3 Segment and Header extraction via Regex.
- Implemented Phase 4 MinGW CMake CI loop.
- Implemented Phase 5 & 6 libclang AST restructuring loop.
- Established strict governance Markdown tracking standards.
