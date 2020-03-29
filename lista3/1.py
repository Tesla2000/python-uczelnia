def transposeFunnyMatrix(matrixArray):
    return [" ".join(row.split(" ")[column] for row in matrixArray) for column in range(len(matrixArray))]


print(transposeFunnyMatrix(["1.1 2.2 3.3", "4.4 5.5 6.6", "7.7 8.8 9.9"]))
