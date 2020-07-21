import sys


def export(fn):
    """ export decorator, c.f. https://stackoverflow.com/a/35710527/8958590 """
    mod = sys.modules[fn.__module__]
    if hasattr(mod, '__all__'):
        mod.__all__.append(fn.__name__)
    else:
        mod.__all__ = [fn.__name__]
    return fn
