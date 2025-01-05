from collections.abc import Sequence
def quickSort(array: Sequence):
    if len(array) == 0:
        return []
    return quickSort([x for x in array[1:] if x < array[0]]) + [array[0]] + quickSort(list(filter(lambda x: x >= array[0], array[1:])))

print(quickSort([2, 3, 4, 6, 7, 1, 2, 1, 2, 3, 8, 9]))
