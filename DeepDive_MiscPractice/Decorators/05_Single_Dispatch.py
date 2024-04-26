from functools import singledispatch
from numbers import Integral
from collections.abc import Sequence


@singledispatch
def worker(v):
    print(f'Default({v})\n')


@worker.register(Integral)
def worker_d(v):
    print(f'Integral({v})\n')


@worker.register(Sequence)
def worker_d(v):
    print(f'Sequence({v})\n')


@worker.register(str)
def worker_d(v):
    print(f'String({v})\n')


@worker.register(bool)
def worker_d(v):
    print(f'Boolean({v})\n')


worker('Hello!')
worker(10)
worker(True)
worker([1, 2, 3])

print(worker.registry)

