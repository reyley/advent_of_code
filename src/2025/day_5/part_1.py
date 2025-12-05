from utils.utils import *


def main(example=False):
    ranges = []
    nums = []
    for line, part in read_split_file(example):
        if part == 1:
            r = line.split("-")
            ranges.append((int(r[0]), int(r[1])))
        if part == 2:
            nums.append(int(line))
    res = 0
    for n in nums:
        for r_min, r_max in ranges:
            if r_min <= n <= r_max:
                res += 1
                break

    print(res)
    return res


assert main(True) == 3
main()