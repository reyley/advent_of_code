from functools import cache

from utils.utils import *


def blink(stone):
    if stone == 0:
        return [1]
    str_stone = str(stone)
    if len(str_stone) % 2 == 0:
        return [int(str_stone[:len(str_stone) // 2]), int(str_stone[ len(str_stone) // 2:])]
    return [stone * 2024]


@cache
def n_stones(stone, n=25):
    res = blink(stone)
    if n == 1:
        return len(res)
    if n > 1:
        return sum(n_stones(s,n-1) for s in res)
    assert False


def main(example=False):
    n_stones.cache_clear()
    stones = []
    for line in read_file(example):
        stones = int_line(line, " ")
    res = sum(n_stones(s) for s in stones)
    print(res)
    return res


assert main(True) == 55312
main()
