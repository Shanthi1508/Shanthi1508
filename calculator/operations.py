"""Arithmetic operations for the calculator package.

Provides fundamental arithmetic functions with strict input validation
and specific error handling.
"""

from typing import Union

Number = Union[int, float]


def _validate_number(value: Number, name: str = "operand") -> Number:
    """Validate that the input is a valid real number (int or float).

    Args:
        value: The value to validate.
        name: Name of the operand for descriptive error messages.

    Returns:
        The validated number.

    Raises:
        TypeError: If value is not an int or float, or if it is a boolean.
    """
    # In Python, bool is a subclass of int (isinstance(True, int) is True).
    # We explicitly exclude bools.
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be an integer or float, got {type(value).__name__}")
    return value


def add(a: Number, b: Number) -> Number:
    """Return the sum of a and b."""
    _validate_number(a, "a")
    _validate_number(b, "b")
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """Return the difference of a and b (a - b)."""
    _validate_number(a, "a")
    _validate_number(b, "b")
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """Return the product of a and b."""
    _validate_number(a, "a")
    _validate_number(b, "b")
    return a * b


def divide(a: Number, b: Number) -> float:
    """Return the quotient of a and b (a / b).

    Raises:
        ZeroDivisionError: If b is 0.
    """
    _validate_number(a, "a")
    _validate_number(b, "b")
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def power(a: Number, b: Number) -> Number:
    """Return a raised to the power of b (a ** b)."""
    _validate_number(a, "a")
    _validate_number(b, "b")
    return a ** b


def modulo(a: Number, b: Number) -> Number:
    """Return the modulo of a and b (a % b).

    Raises:
        ZeroDivisionError: If b is 0.
    """
    _validate_number(a, "a")
    _validate_number(b, "b")
    if b == 0:
        raise ZeroDivisionError("Modulo by zero is not allowed")
    return a % b
