# Using decorators

from functools import reduce


def timed(fn):
    from time import perf_counter
    from functools import wraps

    @wraps(fn)
    def timer(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start

        args_ = [str(a) for a in args]
        kwargs_ = [f'{k}={v}' for k, v in kwargs.items()]
        all_args_str = ', '.join(args_ + kwargs_)

        print(f'Function {fn.__name__}({all_args_str}) took {elapsed:.6f} seconds to run.')

        return result

    return timer


def fib_recursive(n):
    if n <= 2:
        return 1
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)


@timed
def _fib_recursive(n):
    return fib_recursive(n)


@timed
def fib_loop(n):
    fib_1, fib_2 = 1, 1

    for i in range(3, n + 1):
        fib_1, fib_2 = fib_2, fib_1 + fib_2

    return fib_2


@timed
def fib_reduce(n):
    fib = reduce(lambda x, y: (x[1], x[0] + x[1]), range(n-1), (0, 1))
    return fib[1]


print(_fib_recursive(36))
print(fib_loop(36))
print(fib_reduce(36))

