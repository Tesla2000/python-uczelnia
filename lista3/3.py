from os import PathLike
from typing import Union
def sumColumn(path: Union[PathLike[bytes], PathLike[str], bytes, int, str]):
    return sum(int(row.split(' ')[-1]) for row in open(path).readlines())

print(sumColumn('data'))
