from utils.utils import *


def main(example=False):
    ranges = []
    nums = []
    for line, part in read_split_file(example):
        if part == 1:
            r = line.split("-")
            ranges.append((int(r[0]), int(r[1])))
    ranges.sort()
    new_ranges = []

    for r in ranges:
        if not new_ranges or r[0] > new_ranges[-1][1]:
            new_ranges.append(r)
        else:
            new_ranges[-1] = (new_ranges[-1][0], max(new_ranges[-1][1], r[1]))

    res = 0
    for r in new_ranges:
        res += r[1] - r[0] + 1

    print(res)
    return res


assert main(True) == 14
main()