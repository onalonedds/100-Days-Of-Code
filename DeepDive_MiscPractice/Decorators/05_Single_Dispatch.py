from functools import singledispatch
from numbers import Integral
from collections.abc import Sequence


@singledispatch
def worker(v):
    print(f'Default({v})\n')


@worker.register(Integral)
def worker_igl(v):
    print(f'Integral({v})\n')


@worker.register(Sequence)
def worker_sqc(v):
    print(f'Sequence({v})\n')


# @worker.register(str)
# def worker_str(v):
#     print(f'String({v})\n')


# @worker.register(bool)
# def worker_bool(v):
#     print(f'Boolean({v})\n')


worker('Hello!')
worker(10)
worker(True)
worker([1, 2, 3])

for k, v in worker.registry.items():
    print(f'{k.__name__}: {v.__name__}')

