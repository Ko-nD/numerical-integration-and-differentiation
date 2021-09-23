import numpy as np


def test_integral(integral_func):
    assert integral_func(lambda x: x, 0, 10, 0.001) == 50
    assert integral_func(lambda x: x ** 2, 0, 5, 0.001) == 125 / 3

    # Тест на то, что программа не валится
    integral_func(lambda x: 1 / x, -1, 1, 0.001)
    integral_func(lambda x: np.sin(1 / x), -1, 1, 0.001)
