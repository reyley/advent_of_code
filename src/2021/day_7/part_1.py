from statistics import mean

from utils.utils import read_file


def main(example=False):
    res = None
    for line in read_file(example):
        positions = [int(_) for _ in line.split(",")]
        for ans in range(min(positions), max(positions)):
            s = sum(abs(x - ans) for x in positions)
            if res is None:
                res = s
            res = min(res, s)
    print(res)
    return res


assert main(True) == 37
main()
