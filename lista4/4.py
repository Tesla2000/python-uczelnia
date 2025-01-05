from inspect import getfullargspec
from typing import Union

from protocols.protocols import CharSequence

# doesn't work for typed args and default args
class Overloader:
    known_functions = {}

    def __init__(self, func: type):
        Overloader.known_functions[(func.__name__, len(getfullargspec(func).args))] = func
        self.func = func

    def __call__(self, *args, **kwargs):
        return Overloader.known_functions[(self.func.__name__, len(args) + len(kwargs))](*args, **kwargs)

def overload(func):
    return Overloader(func)

@overload
def test(x: int, y: Union[CharSequence, complex, float, int, list, tuple]):
    return x * y

@overload
def test(x):
    return -x

@overload
def test(x, y, z):
    return x + y - z

print(test(100))
print(test(y=2, x=2))
print(test(2, 2, 1))
