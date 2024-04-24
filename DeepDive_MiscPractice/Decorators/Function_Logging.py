# Stacked decorators

import time


def timer(fn):
    from time import perf_counter
    from functools import wraps

    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start

        args_ = [str(a) for a in args]
        kwargs_ = [f'{k}={v}' for k, v in kwargs.items()]
        all_args_str = ', '.join(args_ + kwargs_)

        print(f'Function {fn.__name__}({all_args_str}) took {elapsed:.6f} seconds to run.\n')

        return result

    return inner


def logger(fn):
    from functools import wraps
    from datetime import datetime, timezone

    @wraps(fn)
    def inner(*args, **kwargs):
        run_dt = datetime.now(timezone.utc)
        fn_result = fn(*args, **kwargs)
        print(f'{run_dt}: called {fn.__name__}\n')
        return fn_result

    return inner


@logger
def fn_1():
    time.sleep(0.5)


@logger
def fn_2():
    time.sleep(0.5)


@logger
@timer
def fact(n):
    from operator import mul
    from functools import reduce

    return reduce(mul, range(1, n + 1))


fn_1()
fn_2()
print(fact(3))
