def dispatcher(fn):
    registry = dict()

    registry[object] = fn

    def register(type_):  # decorator factory
        def inner(fn):
            registry[type_] = fn
            return fn  # we do this so we can stack register decorators!

        return inner

    def decorator(arg):  # default decorator
        fn = registry.get(type(arg), registry[object])
        return fn(arg)

    def get_registry():
        for k, v in registry.items():
            print(f'{k.__name__}: {v.__name__}')

    def dispatch(type_):
        return registry.get(type_, registry[object])

    decorator.register = register
    decorator.get_registry = get_registry
    decorator.dispatch = dispatch

    return decorator


@dispatcher
def worker(v):
    print(f'Default({v})\n')


@worker.register(int)
def worker_i(v):
    print(f'Integer({v})\n')


@worker.register(list)
def worker_l(v):
    print(f'List({v})\n')


@worker.register(str)
def worker_s(v):
    print(f'String({v})\n')


@worker.register(bool)
def worker_b(v):
    print(f'Boolean({v})\n')


worker('Hello!')
worker(10)
worker(True)
worker([1, 2, 3])

worker.get_registry()
