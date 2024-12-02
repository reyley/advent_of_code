from utils.utils import *


def is_safe(line):
    if line[1] == line[0]:
        return 0
    pos = line[1] - line[0] > 0
    for i in range(len(line) - 1):
        if line[i+1] - line[i] > 0 and not pos:
            return 0
        if line[i+1] - line[i] < 0 and pos:
            return 0
        if line[i + 1] - line[i] == 0:
            return 0
        if abs(line[i + 1] - line[i]) > 3:
            return 0
    return 1


def main(example=False):
    res = 0
    for line in read_file(example):
        res += is_safe(int_line(line, " "))
    print(res)
    return res


assert main(True) == 2
main()
