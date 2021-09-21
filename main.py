import numpy as np


def get_integral_by_trap(func_, a: float, b: float, step: float):
    x_range: np.ndarray = np.arange(a, b + step, step)
    y_range: np.ndarray = func_(x_range)
    # тут можно вызвать функцию для записи в таблицу arr_X и arr_Y
    y_sum: float = y_range.sum()
    # обрабатываю так NaN и деление на два первого и последнего значения
    if np.isnan(y_range)[0]:
        y_sum -= y_range[0] / 2
    if np.isnan(y_range)[-1]:
        y_sum -= y_range[-1] / 2

    return step * y_sum


def get_derivative_in_point(func_, x, step):
    # формула двусторонней разности
    return (func_(x + step) - func_(x - step)) / (2 * step)


def calc_integral_or_derivative(func_, a, b=None, step=0.1, mode='integral'):
    if mode == 'integral':
        return get_integral_by_trap(func_, a, b, step)
    elif mode == 'derivative':
        # тут можно прописать отдельную функцию для получения arr_X и arr_Y
        # а потом уже одна и та же функция будет записывать значения в таблицу
        # для интегралов и производных
        return get_derivative_in_point(func_, x=a, step=step)
    else:
        raise NotImplemented('Данная операция не поддерживается')


def show_available_functions(file_name, path=''):
    with open(f'{path}{file_name}', 'r') as r_file:
        for line in r_file:
            print(line, end='')


if __name__ == '__main__':
    show_available_functions('functions.txt')
    func = eval('lambda x:' + input('Введите функцию (аргумент x): '))
    i1 = calc_integral_or_derivative(func, -1, 1, 0.001)
    print('Значение интеграла: ', i1)

    func = eval('lambda x:' + input('Введите функцию (аргумент x): '))
    i1 = calc_integral_or_derivative(func, 0, mode='derivative')
    print('Значение производной: ', i1)
