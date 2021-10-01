"""
    Подмодуль для работы с пользователем через консоль
"""

import matplotlib.pyplot as plt


class UI:
    def __init__(self, values_map, funcs):
        self.values = values_map
        self.funcs = funcs

    def ask_value(self, name):
        print(f'Введите {self.values[name]}:')

    def get_value(self, name):
        self.ask_value(name)
        if name == 'mode' or name == 'fun':
            return input()
        else:
            return float(input())

    @staticmethod
    def return_calculated_value(y, mode):
        print(f'Расчитанное значение {"интеграла" if mode == "integral" else "производной"} равно {y}')

    @staticmethod
    def handle_exception(exception, custom_message=None):
        print(custom_message if custom_message else exception.message)

    @staticmethod
    def show_legend(file_name, path=''):
        with open(f'{path}{file_name}', 'r', encoding='utf-8') as r_file:
            for line in r_file:
                print(line, end='')

    def safe_eval(self, fun):
        if fun == '/help':
            UI.show_legend('../functions.txt')
            return 0
        elif fun == '/exit':
            return 1
        elif fun == '/edit':
            return 2
        try:
            return eval('lambda x:' + fun, self.funcs)
        except SyntaxError:
            print('Вы ошиблись в синтаксисе функции!')
            return -1
        except:
            print('Ошибка ввода')
            return -1

    @staticmethod
    def show_graphic(x, y):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        plt.plot(x, y, c='r', marker='o')
        plt.show()
