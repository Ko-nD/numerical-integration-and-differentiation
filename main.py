import matplotlib.pyplot as plt

from calculations import calc_integral_or_derivative
import tests


def show_legend(file_name, path=''):
    with open(f'{path}{file_name}', 'r') as r_file:
        for line in r_file:
            print(line, end='')


def safe_eval(fun):
    if fun == '/help':
        show_legend('functions.txt')
        return 0
    elif fun == '/exit':
        return 1
    return eval('lambda x:' + fun)


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


def main():
    show_legend('functions.txt')
    while True:
        fun = safe_eval(input())
        if fun is 0:
            continue
        elif fun is 1:
            break
        mode = input()
        a = float(input())
        b = float(input())
        step = float(input())
        inf = float(input())
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
