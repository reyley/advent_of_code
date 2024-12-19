from utils.utils import *


def add_towel(towel, towels):
    d = towels
    for ch in towel:
        if ch not in d:
            d[ch] = {}
        d = d[ch]
    d[""] = None

towels = set()
ns = dict()

@cache
def solve(line):
    global towels, ns
    # print(line)
    n = ns[line[0]]
    for i in range(n, 0, -1):
        towel = line[:i]
        if towel in towels:
            if towel == line:
                return True
            else:
                res = solve(line[i:])
                if res:
                    return True
    return False


def main(example=False):
    solve.cache_clear()
    global towels, ns
    towels = set()
    res = 0
    ns = defaultdict(int)
    for line, part in read_split_file(example):
        if part == 1:
            towel_list = line.split(", ")
            for towel in towel_list:
                towels.add(towel)
                ns[towel[0]] = max(ns[towel[0]], len(towel))
        if part == 2:
            print(line)
            if solve(line):
                res += 1
    print(res)
    return res


assert main(True) == 6
main()
