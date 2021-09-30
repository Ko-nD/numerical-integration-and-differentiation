from calculations import calc
import tests
from ui import *


def main(ui: UI):
    ui.show_legend('../functions.txt')
    mode = ui.get_value('mode')
    step = ui.get_value('step')
    inf = ui.get_value('inf')
    while True:
        fun = ui.safe_eval(ui.get_value('fun'))
        if fun == 0 or fun == -1:
            ui.show_legend('../functions.txt')
            continue
        elif fun == 1:
            break
        elif fun == 2:
            mode = ui.get_value('mode')
            step = ui.get_value('step')
            inf = ui.get_value('inf')
        a = ui.get_value('a')
        b = ui.get_value('b')
        if mode == 'integral':
            y = calc(fun, a, b, step, mode, inf)
            ui.return_calculated_value(y, mode)
        else:
            x, y = calc(fun, a, b, step, mode, inf)
            ui.show_graphic(x, y)


if __name__ == '__main__':
    ui = UI({
        'mode': 'Режим расчетов (integral/derivative)',
        'a': 'Нижняя граница интегрирования/дифференцирования',
        'b': 'Верхняя граница интегрирования/дифференцирования',
        'inf': 'Значение, считающееся бесконечностью',
        'step': 'Шаг интегрирования/дифференцирования',
        'fun': 'Функция (от х), по которой необходимо произвести расчет'
    })
    # try:
    tests.test_integral(lambda a, b, c, d: calc(a, b, c, d, 'integral'))
    # except AssertionError as handled_exception:
    #     ui.handle_exception(handled_exception,
    #                         'Будьте осторожны при использовании калькулятора - он может выдавать неверные результаты')

    main(ui)
