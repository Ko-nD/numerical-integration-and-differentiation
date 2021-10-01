import numpy as np

from calculations import calc, get_integral_function, get_derivative_function
import tests
from ui import *


ui_names = {
        'mode': 'Режим расчетов (integral/derivative)',
        'a': 'Нижняя граница интегрирования/дифференцирования',
        'b': 'Верхняя граница интегрирования/дифференцирования',
        'inf': 'Значение, считающееся бесконечностью',
        'step': 'Шаг интегрирования/дифференцирования',
        'fun': 'Функция (от х), по которой необходимо произвести расчет'
}

ui_funcs = {
    'sin': np.sin,
    'cos': np.cos,
    'e': np.exp,
    'log': np.log,
    'tg': np.tan,
    'asin': np.arcsin,
    'acos': np.arccos,
    'atg': np.arctan,
    'integral': get_integral_function,
    'derivative': get_derivative_function
}


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
            _, y = calc(fun, a, b, step, mode, inf)
            ui.return_calculated_value(y, mode)
        else:
            x, y = calc(fun, a, b, step, mode, inf)
            ui.show_graphic(x, y)


if __name__ == '__main__':
    ui = UI(ui_names, ui_funcs)
    main(ui)
