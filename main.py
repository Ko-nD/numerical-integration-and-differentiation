import numpy as np


def get_integral_values_on_range(y_range, step: float):
    y_sum: float = y_range.sum()
    # обрабатываю так NaN и деление на два первого и последнего значения
    if not np.isnan(y_range)[0]:
        y_sum -= y_range[0] / 2
    if not np.isnan(y_range)[-1]:
        y_sum -= y_range[-1] / 2
    return step * y_sum


def get_derivative_values_on_range(y_range, step):
    diff_y_range = np.array([(y_range[i - 1] + y_range[i + 1]) for i in range(1, y_range.shape[0] - 1)])
    # возвращает список значений производной
    return diff_y_range / (2 * step) 


def calc_integral_or_derivative(func_, a, b, step=0.1, mode='integral'):
    x_range: np.ndarray = np.arange(a, b + step, step)
    y_range: np.ndarray = func_(x_range)
    if mode == 'integral':
        return get_integral_values_on_range(y_range, step)
    elif mode == 'derivative':
        # если функция - константа
        if type(y_range == 'int'):
            return 0
        return get_derivative_values_on_range(y_range, step)
    else:
        raise NotImplemented('Данная операция не поддерживается')


def show_legend(file_name, path=''):
    with open(f'{path}{file_name}', 'r') as r_file:
        for line in r_file:
            print(line, end='')


if __name__ == '__main__':
    show_legend('functions.txt')
    func = eval('lambda x:' + input('Введите функцию (аргумент x): '))
    i1 = calc_integral_or_derivative(func, -1, 1, 0.001)
    print('Значение интеграла: ', i1)

    func = eval('lambda x:' + input('Введите функцию (аргумент x): '))
    i1 = calc_integral_or_derivative(func, -1, 1, 0.1, mode='derivative')
    print('Значение производной: ', i1)
