from src.calculations import calc_integral_or_derivative
from src import tests

from src.ui import *


def main():
    show_legend('../functions.txt')
    mode = get_value('mode')
    step = get_value('step')
    inf = get_value('inf')
    while True:
        fun = safe_eval(get_value('fun'))
        if fun == 0 or fun == -1:
            show_legend('../functions.txt')
            continue
        elif fun == 1:
            break
        elif fun == 2:
            mode = get_value('mode')
            step = get_value('step')
            inf = get_value('inf')
        a = get_value('a')
        b = get_value('b')
        try:
            x, y = calc_integral_or_derivative(fun, a, b, step, mode, inf)
            if mode == 'integral':
                return_calculated_value(y, mode)
            else:
                show_graphic(x, y)
        except NotImplemented as handled_exception:
            handle_exception(handled_exception)


if __name__ == '__main__':
    try:
        tests.test_integral(lambda a, b, c, d: calc_integral_or_derivative(a, b, c, d, 'integral'))
    except AssertionError as handled_exception:
        handle_exception(handled_exception,
                         'Будьте осторожны при использовании калькулятора - он может выдавать неверные результаты')
    main()