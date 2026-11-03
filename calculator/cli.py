"""Command-line interface for the calculator package.

Supports:
- Direct expression evaluation: calculator "2 + 3 * 4"
- Interactive REPL mode: calculator
"""

import argparse
import sys
from typing import List, Optional

from calculator.engine import Calculator, evaluate_expression


def run_repl() -> None:
    """Run interactive calculator REPL session."""
    print("Welcome to Simple Calculator!")
    print("Type math expressions (e.g., '2 + 2', '3 * (4 + 5)') or commands:")
    print("  'history' - show calculation history")
    print("  'memory'  - show memory value")
    print("  'mc'      - memory clear")
    print("  'ms'      - memory store current value")
    print("  'mr'      - memory recall")
    print("  'clear'   - reset calculator")
    print("  'exit' or 'quit' - exit calculator\n")

    calc = Calculator()

    while True:
        try:
            line = input("calc> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not line:
            continue

        cmd = line.lower()
        if cmd in ("exit", "quit"):
            print("Goodbye!")
            break
        elif cmd == "history":
            for h in calc.history:
                print(f"  {h}")
            continue
        elif cmd == "memory":
            print(f"Memory: {calc.memory}")
            continue
        elif cmd == "mc":
            calc.memory_clear()
            print("Memory cleared.")
            continue
        elif cmd == "ms":
            calc.memory_store()
            print(f"Stored {calc.memory} into memory.")
            continue
        elif cmd == "mr":
            calc.memory_recall()
            print(f"Result: {calc.value}")
            continue
        elif cmd == "clear":
            calc.reset(0)
            print("Calculator reset to 0.")
            continue

        try:
            calc.calculate(line)
            print(f"Result: {calc.value}")
        except Exception as e:
            print(f"Error: {e}")


def main(argv: Optional[List[str]] = None) -> int:
    """CLI entry point.

    Returns:
        Exit code (0 for success, non-zero for error).
    """
    parser = argparse.ArgumentParser(
        prog="calculator",
        description="A simple, well-structured command-line calculator.",
    )
    parser.add_argument(
        "expression",
        nargs="?",
        default=None,
        help="Mathematical expression to evaluate (e.g., '10 + 5 * 2'). If omitted, starts REPL.",
    )

    args = parser.parse_args(argv)

    if args.expression:
        try:
            result = evaluate_expression(args.expression)
            print(result)
            return 0
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            return 1
    else:
        run_repl()
        return 0


if __name__ == "__main__":
    sys.exit(main())
