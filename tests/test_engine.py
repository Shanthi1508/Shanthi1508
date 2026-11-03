"""Tests for calculator.engine."""

import unittest
from calculator.engine import Calculator, evaluate_expression


class TestEvaluateExpression(unittest.TestCase):
    """Test AST-based expression evaluation."""

    def test_simple_arithmetic(self):
        self.assertEqual(evaluate_expression("1 + 2"), 3)
        self.assertEqual(evaluate_expression("10 - 4"), 6)
        self.assertEqual(evaluate_expression("3 * 5"), 15)
        self.assertEqual(evaluate_expression("12 / 4"), 3.0)
        self.assertEqual(evaluate_expression("2 ** 3"), 8)
        self.assertEqual(evaluate_expression("10 % 3"), 1)
        self.assertEqual(evaluate_expression("7 // 2"), 3)

    def test_precedence_and_grouping(self):
        self.assertEqual(evaluate_expression("2 + 3 * 4"), 14)
        self.assertEqual(evaluate_expression("(2 + 3) * 4"), 20)
        self.assertEqual(evaluate_expression("2 * (3 + 4 * (2 - 1))"), 14)

    def test_unary_operators(self):
        self.assertEqual(evaluate_expression("-5 + 3"), -2)
        self.assertEqual(evaluate_expression("+5 - -3"), 8)
        self.assertEqual(evaluate_expression("-(-4)"), 4)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            evaluate_expression("5 / 0")
        with self.assertRaises(ZeroDivisionError):
            evaluate_expression("5 // 0")
        with self.assertRaises(ZeroDivisionError):
            evaluate_expression("5 % 0")

    def test_syntax_and_unsupported_expressions(self):
        with self.assertRaises(ValueError):
            evaluate_expression("")
        with self.assertRaises(ValueError):
            evaluate_expression("   ")
        with self.assertRaises(ValueError):
            evaluate_expression("2 +")
        with self.assertRaises(ValueError):
            evaluate_expression("__import__('os').system('ls')")
        with self.assertRaises(ValueError):
            evaluate_expression("abs(-5)")
        with self.assertRaises(ValueError):
            evaluate_expression("x + 1")
        with self.assertRaises(TypeError):
            evaluate_expression(123)


class TestCalculatorClass(unittest.TestCase):
    """Test stateful Calculator class."""

    def test_initialization(self):
        calc = Calculator()
        self.assertEqual(calc.value, 0)
        self.assertEqual(calc.memory, 0)
        self.assertEqual(len(calc.history), 1)

        calc_custom = Calculator(10.5)
        self.assertEqual(calc_custom.value, 10.5)

        with self.assertRaises(TypeError):
            Calculator("invalid")

    def test_method_chaining(self):
        calc = Calculator(5)
        result = calc.add(5).multiply(2).subtract(4).divide(2).power(2).modulo(10)
        # 5 + 5 = 10
        # 10 * 2 = 20
        # 20 - 4 = 16
        # 16 / 2 = 8
        # 8 ** 2 = 64
        # 64 % 10 = 4
        self.assertEqual(result.value, 4)
        self.assertIs(result, calc)

    def test_reset(self):
        calc = Calculator(10)
        calc.add(5)
        calc.reset(0)
        self.assertEqual(calc.value, 0)
        calc.reset(42)
        self.assertEqual(calc.value, 42)

    def test_calculate_method(self):
        calc = Calculator()
        calc.calculate("10 + 20 * 2")
        self.assertEqual(calc.value, 50)

    def test_memory_operations(self):
        calc = Calculator(15)
        # Store 15
        calc.memory_store()
        self.assertEqual(calc.memory, 15)

        # Reset value and add to memory
        calc.reset(10)
        calc.memory_add()
        self.assertEqual(calc.memory, 25)

        # Recall memory
        calc.reset(0)
        calc.memory_recall()
        self.assertEqual(calc.value, 25)

        # Clear memory
        calc.memory_clear()
        self.assertEqual(calc.memory, 0)

    def test_history_tracking(self):
        calc = Calculator(2)
        calc.add(3)
        calc.multiply(4)
        history = calc.history
        self.assertEqual(len(history), 3)
        self.assertIn("2 + 3 = 5", history[1])
        self.assertIn("5 * 4 = 20", history[2])

    def test_repr(self):
        calc = Calculator(42)
        self.assertEqual(repr(calc), "Calculator(value=42, memory=0)")


if __name__ == "__main__":
    unittest.main()
