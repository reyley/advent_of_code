from functools import lru_cache
from statistics import mean

from utils.utils import read_file


@lru_cache(maxsize=1000)
def fuel(num):
    return (num * (num + 1)) // 2


def main(example=False):
    res = None
    for line in read_file(example):
        positions = [int(_) for _ in line.split(",")]
        for ans in range(min(positions), max(positions)):
            s = sum(fuel(abs(x - ans)) for x in positions)
            if res is None:
                res = s
            res = min(res, s)
    print(res)
    return res


assert main(True) == 168
main()
