from collections.abc import Iterable
def flatten(funnyList: Iterable):
    for item in funnyList:
        if isinstance(item, list):
            for element in flatten(item):
                yield element
        else:
            yield item
    
print([*flatten([[1, 2, ["a", 4, "b", 5, 5, 5]], [4, 5, 6 ], 7, [[9, [123, [[123]]]], 10]])])
