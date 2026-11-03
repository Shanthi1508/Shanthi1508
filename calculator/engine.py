"""Calculator engine module.

Provides:
- Calculator: Stateful calculator supporting method chaining, history, and memory registers.
- evaluate_expression: Safe AST-based mathematical expression evaluator.
"""

import ast
import operator
from typing import Any, List, Union
from calculator.operations import Number, _validate_number, add, divide, modulo, multiply, power, subtract


_ALLOWED_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
    ast.FloorDiv: operator.floordiv,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}


def _safe_eval_ast(node: ast.AST) -> Number:
    """Safely evaluate an AST expression node containing only arithmetic."""
    if isinstance(node, ast.Expression):
        return _safe_eval_ast(node.body)
    elif isinstance(node, ast.Constant):
        if isinstance(node.value, bool) or not isinstance(node.value, (int, float)):
            raise ValueError(f"Unsupported constant type: {type(node.value).__name__}")
        return node.value
    elif isinstance(node, ast.UnaryOp):
        op_type = type(node.op)
        if op_type not in _ALLOWED_OPERATORS:
            raise ValueError(f"Unsupported unary operator: {op_type.__name__}")
        operand = _safe_eval_ast(node.operand)
        return _ALLOWED_OPERATORS[op_type](operand)
    elif isinstance(node, ast.BinOp):
        op_type = type(node.op)
        if op_type not in _ALLOWED_OPERATORS:
            raise ValueError(f"Unsupported binary operator: {op_type.__name__}")
        left = _safe_eval_ast(node.left)
        right = _safe_eval_ast(node.right)
        if op_type in (ast.Div, ast.FloorDiv, ast.Mod) and right == 0:
            raise ZeroDivisionError("Cannot divide or modulo by zero")
        return _ALLOWED_OPERATORS[op_type](left, right)
    else:
        raise ValueError(f"Unsupported expression syntax: {type(node).__name__}")


def evaluate_expression(expression: str) -> Number:
    """Safely parse and evaluate a mathematical expression string.

    Supports numbers, parentheses, and standard arithmetic operators (+, -, *, /, **, %, //).
    Does NOT use eval(), preventing arbitrary code execution.

    Args:
        expression: The mathematical expression string (e.g., "2 + 3 * (4 - 1)").

    Returns:
        The evaluated result as int or float.

    Raises:
        ValueError: If expression is empty, malformed, or contains invalid syntax.
        ZeroDivisionError: If division or modulo by zero occurs.
    """
    if not isinstance(expression, str):
        raise TypeError(f"Expression must be a string, got {type(expression).__name__}")

    cleaned = expression.strip()
    if not cleaned:
        raise ValueError("Expression cannot be empty")

    try:
        parsed = ast.parse(cleaned, mode="eval")
    except SyntaxError as e:
        raise ValueError(f"Invalid syntax in expression: {expression}") from e

    return _safe_eval_ast(parsed)


class Calculator:
    """Stateful calculator supporting method chaining, history, and memory registers."""

    def __init__(self, initial_value: Number = 0):
        _validate_number(initial_value, "initial_value")
        self._current_value: Number = initial_value
        self._memory: Number = 0
        self._history: List[str] = [f"Initialized with {initial_value}"]

    @property
    def value(self) -> Number:
        """Get current value."""
        return self._current_value

    @property
    def memory(self) -> Number:
        """Get current memory value."""
        return self._memory

    @property
    def history(self) -> List[str]:
        """Get history of calculations."""
        return list(self._history)

    def reset(self, value: Number = 0) -> "Calculator":
        """Reset calculator to a value (default 0)."""
        _validate_number(value, "value")
        self._current_value = value
        self._history.append(f"Reset to {value}")
        return self

    def add(self, value: Number) -> "Calculator":
        """Add value to current value."""
        prev = self._current_value
        self._current_value = add(self._current_value, value)
        self._history.append(f"{prev} + {value} = {self._current_value}")
        return self

    def subtract(self, value: Number) -> "Calculator":
        """Subtract value from current value."""
        prev = self._current_value
        self._current_value = subtract(self._current_value, value)
        self._history.append(f"{prev} - {value} = {self._current_value}")
        return self

    def multiply(self, value: Number) -> "Calculator":
        """Multiply current value by value."""
        prev = self._current_value
        self._current_value = multiply(self._current_value, value)
        self._history.append(f"{prev} * {value} = {self._current_value}")
        return self

    def divide(self, value: Number) -> "Calculator":
        """Divide current value by value."""
        prev = self._current_value
        self._current_value = divide(self._current_value, value)
        self._history.append(f"{prev} / {value} = {self._current_value}")
        return self

    def power(self, value: Number) -> "Calculator":
        """Raise current value to the power of value."""
        prev = self._current_value
        self._current_value = power(self._current_value, value)
        self._history.append(f"{prev} ** {value} = {self._current_value}")
        return self

    def modulo(self, value: Number) -> "Calculator":
        """Modulo current value by value."""
        prev = self._current_value
        self._current_value = modulo(self._current_value, value)
        self._history.append(f"{prev} % {value} = {self._current_value}")
        return self

    def calculate(self, expression: str) -> "Calculator":
        """Evaluate an expression and update current value."""
        result = evaluate_expression(expression)
        self._current_value = result
        self._history.append(f"eval({expression}) = {result}")
        return self

    # Memory functions
    def memory_store(self) -> "Calculator":
        """Store current value in memory."""
        self._memory = self._current_value
        self._history.append(f"Memory store: {self._memory}")
        return self

    def memory_recall(self) -> "Calculator":
        """Set current value to memory value."""
        self._current_value = self._memory
        self._history.append(f"Memory recall: {self._memory}")
        return self

    def memory_clear(self) -> "Calculator":
        """Clear memory (sets to 0)."""
        self._memory = 0
        self._history.append("Memory clear")
        return self

    def memory_add(self) -> "Calculator":
        """Add current value to memory."""
        self._memory = add(self._memory, self._current_value)
        self._history.append(f"Memory add: memory now {self._memory}")
        return self

    def __repr__(self) -> str:
        return f"Calculator(value={self._current_value}, memory={self._memory})"
