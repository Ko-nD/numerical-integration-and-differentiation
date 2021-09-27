def batched_func(operation=lambda a, x: a + x):
    def decorator(fun):
        def wrapper(data, init=0, **kwargs):
            cumulative_value = init
            i = 0
            length = len(data)
            while length >= 1000:
                cumulative_value = operation(cumulative_value, fun(data[i:i+1000], **kwargs))
                i += 1000
                length -= 1000
            if length > 0:
                cumulative_value = operation(cumulative_value, fun(data[i:], **kwargs))
            return cumulative_value
        return wrapper
    return decorator
