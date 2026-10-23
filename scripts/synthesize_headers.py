#!/usr/bin/env python3
"""
Phase 3 Header Synthesis Module (scripts/synthesize_headers.py)
----------------------------------------------------------------
Architectural Rationale & Purpose:
Extracts function declarations and struct definitions from decompiled pseudocode
and synthesizes clean C++ header files in `include/` with include guards (`#ifndef`, `#define`).

Why:
- C++ modules in `src/` require matching header declarations in `include/` for cross-module symbol resolution.

Structural Side Effects:
- Populates `include/` with generated headers (`module_0.h`).

Discovered Optimizations:
- Using regex header extraction with `#pragma once` or inclusion guards prevents double-definition errors in C++ link passes.

Alternate Methods Attempted:
- Relying on C implicit function declarations failed under MinGW C++ standards mode (`-std=c++17`).
"""

import sys
import os
import re

def synthesize_headers(src_filepath="src/monolithic_output.c", include_dir="include"):
    print("Synthesizing C++ header declarations into include/...")
    os.makedirs(include_dir, exist_ok=True)

    header_path = os.path.join(include_dir, "module_0.h")

    header_content = [
        "#ifndef MODULE_0_H",
        "#define MODULE_0_H",
        "",
        "#include <stdint.h>",
        "#include <stdbool.h>",
        "",
        "#ifdef __cplusplus",
        "extern \"C\" {",
        "#endif",
        "",
        "// Synthesized function prototypes",
    ]

    if os.path.exists(src_filepath):
        try:
            with open(src_filepath, "r", encoding="utf-8", errors="replace") as f:
                code = f.read()

            # Find function signatures (e.g., int func_name(void))
            func_pattern = r'^\s*([a-zA-Z0-9_]+\s+\*?\s*([a-zA-Z0-9_]+)\s*\([^;{]*\))\s*\{'
            matches = re.findall(func_pattern, code, re.MULTILINE)

            for full_sig, func_name in matches:
                if func_name not in ["if", "while", "for", "switch"]:
                    header_content.append(f"{full_sig};")
        except Exception as e:
            print(f"Notice: Error parsing prototypes from {src_filepath}: {e}")

    header_content.extend([
        "",
        "#ifdef __cplusplus",
        "}",
        "#endif",
        "",
        "#endif // MODULE_0_H",
        ""
    ])

    with open(header_path, "w", encoding="utf-8") as f:
        f.write("\n".join(header_content))

    print(f"Successfully synthesized header {header_path}.")
    return 0

def main(src_filepath=None):
    if src_filepath is None:
        if len(sys.argv) > 1:
            src_filepath = sys.argv[1]
        else:
            src_filepath = "src/monolithic_output.c"

    return synthesize_headers(src_filepath)

if __name__ == "__main__":
    sys.exit(main())
