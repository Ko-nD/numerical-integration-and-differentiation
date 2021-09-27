"""
    Подмодуль для математических расчетов
"""

import numpy as np
from .aspects.calc_interceptors import batched_func


@batched_func
def get_integral_values_on_range(y_range, step: float, len_x: int) -> float:
    if type(y_range) == int:
        # len_x - 1 это учёт первого и последнего значения
        return y_range * step * (len_x - 1)
    y_sum: float = y_range.sum()
    # обрабатываю так NaN и деление на два первого и последнего значения
    if not np.isnan(y_range)[0]:
        y_sum -= y_range[0] / 2
    if not np.isnan(y_range)[-1]:
        y_sum -= y_range[-1] / 2
    return step * y_sum


@batched_func(operation=lambda a, x: np.concatenate(a, x))
def get_derivative_values_on_range(y_range, step: float, len_x: int) -> np.ndarray:
    if type(y_range) == int:
        return np.array([0] * len_x)
    diff_y_range = np.array([np.nansum([y_range[i + 1], - y_range[i - 1]]) for i in range(1, y_range.shape[0] - 1)])
    # возвращает список значений производной
    return diff_y_range / (2 * step)


def calc(func_, a, b, step=0.1, mode='integral', inf=10e5):
    x_range: np.ndarray = np.arange(a, b + step, step)
    if mode == 'derivative':
        x_range = np.concatenate((a - step, x_range, b + step), axis=None)
    len_x = x_range.shape[0]
    y_range: np.ndarray = func_(x_range)
    if not type(y_range == int):
        y_range += np.array([0 if y_range[i] < inf else np.inf for i in range(len(y_range))])
    if mode == 'integral':
        return x_range, get_integral_values_on_range(y_range, step, len_x)
    elif mode == 'derivative':
        return x_range[1:-1], get_derivative_values_on_range(y_range, step, len_x)
    else:
        raise NotImplemented('Данная операция не поддерживается')


def get_integral_function(func_, step=0.1, inf=10e5):
    return lambda x: calc(func_, 0, x, step=step, inf=inf)
