"""A simple, extensible, and well-structured calculator package."""

from calculator.engine import Calculator, evaluate_expression
from calculator.operations import add, divide, modulo, multiply, power, subtract

__version__ = "0.1.0"
__all__ = [
    "Calculator",
    "evaluate_expression",
    "add",
    "subtract",
    "multiply",
    "divide",
    "power",
    "modulo",
]
