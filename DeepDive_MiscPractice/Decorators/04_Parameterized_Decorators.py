def timed(reps):
    def timer(fn):
        from functools import wraps
        from time import perf_counter

        @wraps(fn)
        def inner(*args, **kwargs):
            total_elapsed = 0
            result = None

            for i in range(reps):
                start = perf_counter()
                result = fn(*args, **kwargs)
                end = perf_counter()
                total_elapsed += end - start

            avg_run_time = total_elapsed / reps

            args_ = [str(a) for a in args]
            kwargs_ = [f'{k}={v}' for k, v in kwargs.items()]
            all_args_str = ', '.join(args_ + kwargs_)

            print(f'Avg run time of {fn.__name__}({all_args_str}) is {avg_run_time:.6f}s')
            return result

        return inner

    return timer


def calc_fib_recurse(n):
    return 1 if n < 3 else calc_fib_recurse(n-1) + calc_fib_recurse(n-2)


@timed(5)
def fib(n):
    return calc_fib_recurse(n)


fib(30)
