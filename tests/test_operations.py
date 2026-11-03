"""Tests for calculator.operations."""

import math
import unittest
from calculator.operations import (
    _validate_number,
    add,
    divide,
    modulo,
    multiply,
    power,
    subtract,
)


class TestOperations(unittest.TestCase):
    """Test arithmetic operations and edge cases."""

    def test_validation_valid(self):
        self.assertEqual(_validate_number(10), 10)
        self.assertEqual(_validate_number(-3.5), -3.5)
        self.assertEqual(_validate_number(0), 0)

    def test_validation_invalid(self):
        with self.assertRaises(TypeError):
            _validate_number("123")
        with self.assertRaises(TypeError):
            _validate_number(True)  # bool should not be treated as int
        with self.assertRaises(TypeError):
            _validate_number(None)
        with self.assertRaises(TypeError):
            _validate_number([1, 2])

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-5, -5), -10)
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=7)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(4, 10), -6)
        self.assertEqual(subtract(0, 0), 0)
        self.assertAlmostEqual(subtract(5.5, 2.2), 3.3, places=7)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 5), -10)
        self.assertEqual(multiply(-3, -3), 9)
        self.assertEqual(multiply(100, 0), 0)
        self.assertAlmostEqual(multiply(2.5, 4), 10.0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5.0)
        self.assertEqual(divide(-9, 3), -3.0)
        self.assertAlmostEqual(divide(1, 3), 1 / 3)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)
        with self.assertRaises(ZeroDivisionError):
            divide(0, 0)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(2, -1), 0.5)
        self.assertAlmostEqual(power(9, 0.5), 3.0)

    def test_modulo(self):
        self.assertEqual(modulo(10, 3), 1)
        self.assertEqual(modulo(20, 5), 0)
        self.assertAlmostEqual(modulo(7.5, 2), 1.5)

    def test_modulo_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            modulo(10, 0)

    def test_type_errors(self):
        with self.assertRaises(TypeError):
            add("a", 1)
        with self.assertRaises(TypeError):
            subtract(1, "b")
        with self.assertRaises(TypeError):
            multiply(None, 2)
        with self.assertRaises(TypeError):
            divide(1, True)
        with self.assertRaises(TypeError):
            power("2", 3)
        with self.assertRaises(TypeError):
            modulo(5, [1])


if __name__ == "__main__":
    unittest.main()
