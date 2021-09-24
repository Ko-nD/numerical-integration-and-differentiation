from calculations import calc_integral_or_derivative
import tests

from ui import *


def main():
    show_legend('functions.txt')
    mode = get_value('mode')
    step = get_value('step')
    inf = get_value('inf')
    while True:
        fun = safe_eval(get_value('fun'))
        if fun is 0:
            continue
        elif fun is 1:
            break
        elif fun is 2:
            mode = get_value('mode')
            step = get_value('step')
            inf = get_value('inf')
        a = get_value('a')
        b = get_value('b')
        try:
            x, y = calc_integral_or_derivative(fun, a, b, step, mode, inf)
            if mode == 'integral':
                print(y)
            else:
                show_graphic(x, y)
        except NotImplemented as handled_exception:
            print(handled_exception.message)


if __name__ == '__main__':
    try:
        tests.test_integral(lambda a, b, c, d: calc_integral_or_derivative(a, b, c, d, 'integral'))
    except AssertionError:
        print('Будьте осторожны при использовании калькулятора - он может выдавать неверные результаты')
    main()
