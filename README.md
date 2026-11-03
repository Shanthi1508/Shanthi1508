# Simple Calculator

A modular, well-structured Python calculator package featuring basic arithmetic operations, a stateful calculation engine with method chaining and memory registers, safe AST-based mathematical expression parsing, and an interactive CLI / REPL.

---

## Architecture & Directory Structure

```text
.
├── calculator/                 # Main package directory
│   ├── __init__.py             # Public API exports and versioning
│   ├── __main__.py             # Entry point for `python -m calculator`
│   ├── cli.py                  # Interactive REPL and command-line evaluator
│   ├── engine.py               # Stateful Calculator class & AST expression evaluator
│   └── operations.py           # Core arithmetic functions and input validation
├── tests/                      # Automated test suite
│   ├── __init__.py
│   ├── test_cli.py             # CLI tests (arguments and REPL session)
│   ├── test_engine.py          # Engine tests (chaining, memory, history, AST eval)
│   └── test_operations.py      # Operations tests (math, validation, zero division)
├── pyproject.toml              # Packaging configuration & CLI console script
└── README.md                   # Documentation
```

---

## Features

- **Strict Input Validation**: Rejects invalid types, non-numeric values, and booleans.
- **Safe Expression Evaluation**: Uses Python's `ast` parser to safely evaluate arithmetic expressions without using dangerous `eval()`.
- **Stateful Engine & Fluent API**: Method chaining for operations (`calc.add(5).multiply(2)...`).
- **Memory Registers**: Store (`ms`), Recall (`mr`), Add (`m+`), and Clear (`mc`).
- **Calculation History**: Audit trail of steps and operations performed.
- **Interactive CLI & One-Shot Mode**: Run direct command-line calculations or launch an interactive REPL.

---

## Installation

Install in editable mode using `pip`:

```bash
pip install -e .
```

---

## Usage

### 1. Command-Line Interface (CLI)

#### Direct Expression Evaluation
```bash
python3 -m calculator "2 + 3 * (4 - 1)"
# or if installed:
calculator "2 + 3 * (4 - 1)"
```
Output:
```text
11
```

#### Interactive REPL Mode
Run without arguments to start the interactive calculator:
```bash
python3 -m calculator
```
Example session:
```text
Welcome to Simple Calculator!
Type math expressions (e.g., '2 + 2', '3 * (4 + 5)') or commands:
  'history' - show calculation history
  'memory'  - show memory value
  'mc'      - memory clear
  'ms'      - memory store current value
  'mr'      - memory recall
  'clear'   - reset calculator
  'exit' or 'quit' - exit calculator

calc> 15 * 4
Result: 60
calc> ms
Stored 60 into memory.
calc> clear
Calculator reset to 0.
calc> 20 + 5
Result: 25
calc> mr
Result: 60
calc> history
  Initialized with 0
  eval(15 * 4) = 60
  Memory store: 60
  Reset to 0
  eval(20 + 5) = 25
  Memory recall: 60
calc> exit
Goodbye!
```

---

### 2. Python Library Usage

#### Direct Operations
```python
from calculator import add, subtract, multiply, divide, power, modulo

print(add(10, 5))        # 15
print(multiply(4, 2.5))  # 10.0
print(divide(20, 4))     # 5.0
```

#### Safe Expression Evaluation
```python
from calculator import evaluate_expression

result = evaluate_expression("10 + 2 ** 3 * (5 - 2)")
print(result)  # 34
```

#### Stateful Calculator with Method Chaining
```python
from calculator import Calculator

calc = Calculator(10)
calc.add(5).multiply(2).subtract(4).divide(2)
print(calc.value)  # 13.0

# Memory Operations
calc.memory_store()
calc.reset(0)
calc.memory_recall()
print(calc.value)  # 13.0
print(calc.history)
```

---

## Running Tests

Run the test suite using `unittest`:

```bash
python3 -m unittest discover tests -v
```
