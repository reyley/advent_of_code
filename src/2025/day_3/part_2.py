from utils.utils import *


def get_joltage(line, n=2):
    digits = []
    for i in range(n):
        digit = max(list(line[:len(line) - (n - i - 1)]))
        digit_index = line.index(digit)
        line = line[digit_index + 1:]
        digits.append(digit)
    return int("".join(digits))


def main(example=False):
    res = 0
    for line in read_file(example):
        res += get_joltage(line, 12)
    print(res)
    return res


assert main(True) == 3121910778619
main()