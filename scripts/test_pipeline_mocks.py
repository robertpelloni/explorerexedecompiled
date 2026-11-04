import unittest
import os
import io
import contextlib
import synthesize_ast_blocks
import segment_c
import refine_c
import synthesize_headers

class TestPipelineMocks(unittest.TestCase):
    def setUp(self):
        self.test_dir = "test_mock_data"
        os.makedirs(self.test_dir, exist_ok=True)
        self.dummy_file = os.path.join(self.test_dir, "dummy.c")
        with open(self.dummy_file, "w") as f:
            f.write("undefined4 main(void) { undefined8 x = 0; return 0; }\n")

    def tearDown(self):
        for f in os.listdir(self.test_dir):
            os.remove(os.path.join(self.test_dir, f))
        os.rmdir(self.test_dir)

    def test_refine_c(self):
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            result = refine_c.main(self.dummy_file)

        self.assertEqual(result, 0)
        with open(self.dummy_file, "r") as f_in:
            content = f_in.read()
        self.assertIn("uint32_t main", content)
        self.assertIn("uint64_t x", content)
        self.assertIn("#include <stdint.h>", content)

    def test_refine_c_missing_file(self):
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            result = refine_c.main("nonexistent.c")

        self.assertEqual(result, 0)
        output = f.getvalue()
        self.assertIn("Notice:", output)

    def test_synthesize_headers(self):
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            result = synthesize_headers.main(self.dummy_file)

        self.assertEqual(result, 0)
        self.assertTrue(os.path.exists("include/module_0.h"))

    def test_ast_blocks(self):
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            result = synthesize_ast_blocks.main(self.dummy_file)

        output = f.getvalue()
        self.assertEqual(result, 0)
        self.assertIn("Mock: Parsed", output)
        self.assertIn("Mock: Rewriting goto", output)

    def test_ast_blocks_missing_file(self):
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            result = synthesize_ast_blocks.main("nonexistent.c")

        output = f.getvalue()
        self.assertEqual(result, 1)
        self.assertIn("ERROR:", output)

    def test_segment_c(self):
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            result = segment_c.main(self.dummy_file)

        output = f.getvalue()
        self.assertEqual(result, 0)
        self.assertIn("Successfully segmented pseudocode", output)

    def test_segment_c_missing_file(self):
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            result = segment_c.main("nonexistent.c")

        output = f.getvalue()
        self.assertEqual(result, 0)
        self.assertIn("Notice:", output)

    def test_deeply_nested_gotos(self):
        nested_file = os.path.join(self.test_dir, "nested.c")
        with open(nested_file, "w") as f:
            code = "int main() {\n"
            for i in range(50):
                code += f"L_{i}:\n"
            code += "goto L_0;\nreturn 0; }"
            f.write(code)

        f_out = io.StringIO()
        with contextlib.redirect_stdout(f_out):
            result = synthesize_ast_blocks.main(nested_file)

        output = f_out.getvalue()
        self.assertEqual(result, 0)
        self.assertIn("Mock: Parsed", output)

    def test_malformed_c_structs(self):
        malformed_file = os.path.join(self.test_dir, "malformed.c")
        with open(malformed_file, "w") as f:
            f.write("struct Invalid { int x; int y } // missing semicolon\nint main() { return 0; }")

        f_out = io.StringIO()
        with contextlib.redirect_stdout(f_out):
            result = synthesize_ast_blocks.main(malformed_file)

        output = f_out.getvalue()
        self.assertEqual(result, 0)
        self.assertIn("Mock: Parsed", output)

    def test_transpile_to_rust(self):
        f = io.StringIO()
        import transpile_to_rust
        with contextlib.redirect_stdout(f):
            result = transpile_to_rust.main(self.dummy_file)

        output = f.getvalue()
        self.assertEqual(result, 0)
        self.assertIn("unsafe fn mock_entry", output)
        self.assertIn("Transpiling AST to Rust", output)

    def test_generate_custom_shell(self):
        f = io.StringIO()
        import generate_custom_shell
        with contextlib.redirect_stdout(f):
            result = generate_custom_shell.main()

        output = f.getvalue()
        self.assertEqual(result, 0)
        self.assertIn("Generating Custom Shell Variations", output)
        self.assertIn("kiosk_shell.exe", output)

    def test_generate_plugin_architecture(self):
        f = io.StringIO()
        import generate_plugin_architecture
        with contextlib.redirect_stdout(f):
            result = generate_plugin_architecture.main()

        output = f.getvalue()
        self.assertEqual(result, 0)
        self.assertIn("Generating Plugin Architecture", output)
        self.assertIn("plugin-based shell architecture", output)

    def test_generate_ast_graph(self):
        f = io.StringIO()
        import generate_ast_graph
        with contextlib.redirect_stdout(f):
            result = generate_ast_graph.main()

        output = f.getvalue()
        self.assertEqual(result, 0)
        self.assertIn("Generating AST Visualization Graph", output)
        self.assertIn("ast_graph.dot", output)

    def test_generate_vulnerability_report(self):
        f = io.StringIO()
        import generate_vulnerability_report
        with contextlib.redirect_stdout(f):
            result = generate_vulnerability_report.main()

        output = f.getvalue()
        self.assertEqual(result, 0)
        self.assertIn("Generating Vulnerability Report", output)
        self.assertIn("vulnerability_report.json", output)

    def test_generate_ai_summary(self):
        f = io.StringIO()
        import generate_ai_summary
        with contextlib.redirect_stdout(f):
            result = generate_ai_summary.main()

        output = f.getvalue()
        self.assertEqual(result, 0)
        self.assertIn("Generating AI Code Summaries", output)
        self.assertIn("Injected human-readable docstrings", output)

if __name__ == "__main__":
    unittest.main()
