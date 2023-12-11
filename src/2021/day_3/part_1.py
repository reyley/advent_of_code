from utils.utils import read_file
from collections import defaultdict


def convert_binary(binary_str):
    res = 0
    for i, chr in enumerate(reversed(binary_str)):
        res += int(chr) * 2 ** i
    return res


def calculate_res(zero_count, one_count):
    binary_gamma = ""
    binary_epsilon = ""
    for i in range(len(zero_count)):
        if zero_count[i] > one_count[i]:
            binary_gamma += "0"
            binary_epsilon += "1"
        else:
            binary_gamma += "1"
            binary_epsilon += "0"
    return convert_binary(binary_gamma) * convert_binary(binary_epsilon)


def main(example=False):
    zero = None
    one = None
    for line in read_file(example):
        if zero is None:
            zero = [0] * len(line)
            one = [0] * len(line)
        for i, chr in enumerate(line):
            if chr == "0":
                zero[i] += 1
            elif chr == "1":
                one[i] += 1

    res = calculate_res(zero, one)
    print(res)
    return res


assert main(True) == 198
main()
