import numpy as np


def wrapped_file_write(file, text):
    file.write(text)
    return file


def batched_func(operation=lambda a, x: a + x, init=0):
    def decorator(fun):
        def wrapper(data, *args, **kwargs):
            cumulative_value = init
            i = 0
            length = len(data)
            op = operation
            if length > 1000000 and type(init) == np.ndarray:
                cumulative_value = open('derivative.csv', 'a')
                op = wrapped_file_write
            while length >= 1000:
                cumulative_value = op(cumulative_value, fun(data[i:i+1000], *args, **kwargs))
                i += 1000
                length -= 1000
            if length > 0:
                cumulative_value = op(cumulative_value, fun(data[i:], *args, **kwargs))
            return cumulative_value
        return wrapper
    return decorator
