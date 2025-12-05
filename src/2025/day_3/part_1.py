from utils.utils import *


def get_joltage(line):
    first_digit = max(list(line[:-1]))
    first_digit_index = line.index(first_digit)
    last_digit = max(list(line[first_digit_index + 1:]))
    return int(first_digit + last_digit)


def main(example=False):
    res = 0
    for line in read_file(example):
        res += get_joltage(line)
    print(res)
    return res


assert main(True) == 357
main()