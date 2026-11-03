"""Tests for calculator.cli."""

import io
import unittest
from unittest.mock import patch

from calculator.cli import main, run_repl


class TestCLI(unittest.TestCase):
    """Test CLI commands and REPL mode."""

    def test_direct_expression_success(self):
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            exit_code = main(["3 * 5 + 2"])
            self.assertEqual(exit_code, 0)
            self.assertEqual(mock_stdout.getvalue().strip(), "17")

    def test_direct_expression_error(self):
        with patch("sys.stderr", new_callable=io.StringIO) as mock_stderr:
            exit_code = main(["10 / 0"])
            self.assertNotEqual(exit_code, 0)
            self.assertIn("Cannot divide or modulo by zero", mock_stderr.getvalue())

    def test_direct_expression_invalid_syntax(self):
        with patch("sys.stderr", new_callable=io.StringIO) as mock_stderr:
            exit_code = main(["3 +* 2"])
            self.assertNotEqual(exit_code, 0)
            self.assertIn("Invalid syntax", mock_stderr.getvalue())

    def test_repl_commands(self):
        inputs = iter([
            "2 + 2",
            "ms",
            "memory",
            "clear",
            "mr",
            "history",
            "mc",
            "exit",
        ])
        with patch("builtins.input", side_effect=inputs), \
             patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            run_repl()
            output = mock_stdout.getvalue()
            self.assertIn("Result: 4", output)
            self.assertIn("Stored 4 into memory", output)
            self.assertIn("Memory: 4", output)
            self.assertIn("Calculator reset to 0.", output)
            self.assertIn("Result: 4", output)
            self.assertIn("Memory cleared.", output)
            self.assertIn("Goodbye!", output)

    def test_repl_error_handling(self):
        inputs = iter([
            "10 / 0",
            "exit",
        ])
        with patch("builtins.input", side_effect=inputs), \
             patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            run_repl()
            output = mock_stdout.getvalue()
            self.assertIn("Error: Cannot divide or modulo by zero", output)
            self.assertIn("Goodbye!", output)


if __name__ == "__main__":
    unittest.main()
