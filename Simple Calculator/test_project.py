# test_project.py
import pytest
from project import perform_arithmetic_operation, square, square_root, factorial


def test_addition():
    assert perform_arithmetic_operation("1", 5, 3) == 8


def test_subtraction():
    assert perform_arithmetic_operation("2", 5, 3) == 2


def test_multiplication():
    assert perform_arithmetic_operation("3", 5, 3) == 15


def test_division():
    assert perform_arithmetic_operation("4", 6, 3) == 2


def test_square():
    result1, result2 = square(4, 3)
    assert result1 == 16
    assert result2 == 9


def test_square_root():
    result1, result2 = square_root(16, 9)
    assert result1 == 4
    assert result2 == 3


def test_factorial():
    result1, result2 = factorial(5, 3)
    assert result1 == 120
    assert result2 == 6


def test_invalid_factorial():
    assert factorial(2.5, -1) == (
        "Factorial is only defined for non-negative integers.",
        "Factorial is only defined for non-negative integers.",
    )
