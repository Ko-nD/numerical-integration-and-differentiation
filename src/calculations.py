"""
    Подмодуль для математических расчетов
"""

import numpy as np


def get_integral_values_on_range(y_range, step: float, len_x: int):
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


def get_derivative_values_on_range(y_range, step: float, len_x: int):
    if type(y_range) == int:
        return np.array([0] * len_x)
    diff_y_range = np.array([np.nansum([y_range[i + 1], - y_range[i - 1]]) for i in range(1, y_range.shape[0] - 1)])
    # возвращает список значений производной
    return diff_y_range / (2 * step)


def calc_integral_or_derivative(func_, a, b, step=0.1, mode='integral', inf=10e5):
    x_range: np.ndarray = np.arange(a, b + step, step)
    len_x = x_range.shape[0]
    y_range: np.ndarray = func_(x_range)
    y_range += np.array([0 if y_range[i] < inf else np.inf for i in range(len(y_range))])
    if mode == 'integral':
        return x_range, get_integral_values_on_range(y_range, step, len_x)
    elif mode == 'derivative':
        return x_range, get_derivative_values_on_range(y_range, step, len_x)
    else:
        raise NotImplemented('Данная операция не поддерживается')


def calc(func_, a, b, step=0.1, mode='integral', inf=10e5):
    def calc_cum_val(cum_val, a, b):
        val = calc_integral_or_derivative(func_, a, b, step, mode, inf)
        if mode == 'integral':
            return cum_val + val
        else:
            return np.concatenate(cum_val, val)

    length = abs(b - a) / step
    cum_val = 0 if mode == 'integral' else np.array([])
    i = a
    while length >= 1000:
        cum_val = calc_cum_val(cum_val, i, i+step*1000)
        length -= 1000
        i += step * 1000
    if length > 0:
        cum_val = calc_cum_val(cum_val, i, b)
    return cum_val



def get_integral_function(func_, step=0.1, inf=10e5):
    return lambda x: calc_integral_or_derivative(func_, 0, x, step=step, inf=inf)
