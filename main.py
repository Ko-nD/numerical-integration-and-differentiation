import numpy as np
from math import *


def get_func_value(func, x):
    try:
        y = func(x)
    except ArithmeticError:
        return None
    return y
    
    
def get_integral_by_trap(func, a, b, step):
    arr_X = np.arange(a, b + step, step)
    arr_Y = [get_func_value(func, x) for x in arr_X]
    # тут можно вызвать функцию для записи в таблицу arr_X и arr_Y
    y_sum = 0
    # обрабатываю так None и деление на два первого и последнего значения
    for value in arr_Y:
        if value != None: y_sum += value
    if arr_Y[0] != None: y_sum -= arr_Y[0] / 2
    if arr_Y[-1] != None: y_sum -= arr_Y[-1] / 2
            
    return step * y_sum
            


def get_derivative_in_point(func, x, step):
    if get_func_value(func, x) == None:
        return None
    # формула двусторонней разности
    return (get_func_value(func, x + step) - get_func_value(func, x - step)) / (2 * step)
    


def culc_integral_or_derivative(func, a, b=None, step=0.1, typ='integral'):
    if typ == 'integral':
        return get_integral_by_trap(func, a, b, step)
    if typ == 'derivative':
        # тут можно прописать отдельную функцию для получения arr_X и arr_Y
        # а потом уже одна и та же функция будет записывать значения в таблицу
        # для интегралов и производных
        return get_derivative_in_point(func, x=a, step=step)
    pass


def show_available_functions(file_name, path=''):
    with open(f'{path}{file_name}', 'r') as r_file:
        for line in r_file: print(line, end='')
        


show_available_functions('functions.txt')
func = eval('lambda x:' + input('Введите функцию (аргумент x): '))
i1 = culc_integral_or_derivative(func, -1, 1, 0.001)
print('Значение интеграла: ', i1)

func = eval('lambda x:' + input('Введите функцию (аргумент x): '))
i1 = culc_integral_or_derivative(func, 0, typ='derivative')
print('Значение производной: ', i1)