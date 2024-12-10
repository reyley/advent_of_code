from functools import cache

from utils.utils import *


class Map:
    n_rows = 0
    n_cols = 0
    map = {}

    @classmethod
    def add(cls, r,c,ch):
        if r == 0 == c:
            cls.reset()
        cls.map[(r,c)] = int(ch)
        cls.n_rows = max(cls.n_rows, r+1)
        cls.n_cols = max(cls.n_cols, c + 1)

    @classmethod
    def get(cls,x):
        try:
            return cls.map[x]
        except:
            return None

    @classmethod
    def reset(cls):
        cls.n_rows = 0
        cls.n_cols = 0
        cls.map = {}


@cache
def get_ends(x):
    level = Map.get(x)
    if level == 9:
        return {x}
    ends = set()
    for n in traverse_neighbors(x):
        if Map.get(n) == level + 1:
            ends.update(get_ends(n))
    return ends


def count_trails(s):
    ends = get_ends(s)
    return len(ends)


def main(example=False):
    get_ends.cache_clear()
    starts = set()
    for r,c,ch in read_map(example):
        Map.add(r,c,ch)
        if ch == "0":
            starts.add((r,c))
    res = 0
    for s in starts:
        c = count_trails(s)
        print(c)
        res += c
    print(res)
    return res


assert main(True) == 36
main()
