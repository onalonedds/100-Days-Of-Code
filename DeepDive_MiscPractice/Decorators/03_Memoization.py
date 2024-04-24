# Option 1: using a class

class Fib:
    def __init__(self):
        self.cache = {1: 1, 2: 1}

    def fib(self, n):
        if n not in self.cache:
            print(f'Calculating fib({n})...')
            self.cache[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.cache[n]


f1 = Fib()
# print(f1.fib(10), '\n')


# Option 2: using a closure

def fib_cl():
    cache = {1: 1, 2: 1}

    def calc_fib(n):
        if n not in cache:
            print(f'Calculating fib({n})...')
            cache[n] = calc_fib(n - 1) + calc_fib(n - 2)
        return cache[n]

    return calc_fib


f2 = fib_cl()
# print(f2(10), '\n')


# Option 3: using decorator

def memoize(fn):
    cache = dict()

    def inner(n):
        if n not in cache:
            cache[n] = fn(n)
        return cache[n]

    return inner


@memoize
def fib(n):
    print(f'Calculating fib({n})...')
    return 1 if n < 3 else fib(n - 1) + fib(n - 2)


@memoize
def fact(n):
    print(f'Calculating {n}!...')
    return 1 if n < 2 else n * fact(n-1)


# print(fib(10))
# print(fib(10))  # No calculations are needed this time
# print(fib(11), '\n')  # Just one calculation is needed
#
# print(fact(10))
# print(fact(11))


# Option 4: using built-in module 'lru_cache' - least recently used cache

from functools import lru_cache


@lru_cache(maxsize=8)
def fib2(n):
    print(f'Calculating fib({n})...')
    return 1 if n < 3 else fib2(n - 1) + fib2(n - 2)


print(fib2(8))
print(fib2(8))
print(fib2(9))
print(fib2(1))  # fib2(1) was replaced by fib2(9) and needs to be recalculated
