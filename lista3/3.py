def sumColumn(path):
    return sum(int(row.split(' ')[-1]) for row in open(path).readlines())

print(sumColumn('data'))