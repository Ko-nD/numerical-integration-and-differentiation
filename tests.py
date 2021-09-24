"""
    Подмодуль для тестирования
"""

import numpy as np


def equals(a, b, accuracy=0.001):
    return abs(a-b) < accuracy


def test_integral(integral_func):
    assert integral_func(lambda x: x, 0, 10, 0.001) == 50
    assert equals(integral_func(lambda x: x ** 2, 0, 5, 0.001), 125 / 3)
    assert equals(integral_func(lambda x: np.exp(-x**2), -1, 1, 0.001), 2.925)

    # Тест на то, что программа не валится
    integral_func(lambda x: 1 / x, -1, 1, 0.001)
    integral_func(lambda x: np.sin(1 / x), -1, 1, 0.001)
