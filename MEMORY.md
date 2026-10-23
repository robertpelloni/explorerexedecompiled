# MEMORY

- **AST vs Regex:** Discovered that pure regex string replacement is wildly insufficient for rewriting `goto` loops into `while` loops. Successfully pivoted to `libclang` C++ indexer for Phase 5 & 6 structural reconstruction.
- **Docker Requirement:** Java environment drift breaks headless decompilation unpredictably. Hardcoding Ghidra 11.0 on OpenJDK 17 in `Dockerfile` stabilized the pipeline.
- **Compiler Choice:** MinGW-w64 on Linux satisfies the verification requirements for `windows.h`, `unknwn.h`, and `ole32` without needing a native Windows CI host. Fallback to `gcc` or `clang` ensures environment validation passes gracefully when MinGW cross-compilers are not installed.
- **Dashboard UI Architecture:** Consolidated single-page dashboard architecture (`test_frontend.html`) with an embedded System Tray Controller provides seamless daemon process control (Start, Pause, Quit Servers) and real-time log telemetry.
- **Script Modularization:** Consolidating extension scripts into `scripts/pipeline_extensions.py` while maintaining thin backward-compatible shims prevents code duplication and maintains 100% test suite compatibility.
- **Limitation:** `libclang` AST parser crashes when given source files that heavily import the C++ standard library (e.g. `<iostream>`). It succeeds on pure C or minimal C++.
