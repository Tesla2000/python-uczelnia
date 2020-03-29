def subsets(array):
    if len(array) == 0:
        return [[]]
    return subsets(array[1:]) + list(map(lambda x: [array[0]] + x, subsets(array[1:])))

print(subsets([1, 2, 3]))
