"""
    Подмодуль для работы с пользователем через консоль
"""

import matplotlib.pyplot as plt


VALUES = {
    'mode': 'Режим расчетов (integral/derivative)',
    'a': 'Нижняя граница интегрирования/дифференцирования',
    'b': 'Верхняя граница интегрирования/дифференцирования',
    'inf': 'Значение, считающееся бесконечностью',
    'step': 'Шаг интегрирования/дифференцирования',
    'fun': 'Функция, по которой необходимо произвести расчет'
}


def ask_value(name):
    print(f'Введите значение {VALUES[name]}')


def get_value(name):
    ask_value(name)
    if name == 'mode' or name == 'fun':
        return input()
    else:
        return float(input())


def return_calculated_value(y, mode):
    print(f'Расчитанное значение {"интеграла" if mode == "integral" else "производной"} равно {y}')


def handle_exception(exception, custom_message=None):
    print(custom_message if custom_message else exception.message)


def show_legend(file_name, path=''):
    with open(f'{path}{file_name}', 'r') as r_file:
        for line in r_file:
            print(line, end='')


def safe_eval(fun):
    if fun == '/help':
        show_legend('../functions.txt')
        return 0
    elif fun == '/exit':
        return 1
    elif fun == '/edit':
        return 2
    try:
        return eval('lambda x:' + fun)
    except SyntaxError:
        print('Вы ошиблись в синтаксисе функции!')
        return -1
    except:
        print('Ошибка ввода')
        return -1


def show_graphic(x, y):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    plt.plot(x, y, 'r')
    plt.show()
