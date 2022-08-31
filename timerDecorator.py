from time import perf_counter
import functools

def timeCalc(func):


    @functools.wraps(func)
    def wrapper(*args, **kargs):

        t1 = perf_counter()
        output = func(*args, **kargs)
        t2 = perf_counter()
        print(f'Time needed to run {func.__name__} was {t2 - t1:.4}')
        return output

    return wrapper

        