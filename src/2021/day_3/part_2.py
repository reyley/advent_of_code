import bisect

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


def get_number(numbers, comp, default):
    i = 0
    start = 0
    end = len(numbers)
    while end - start > 1:
        mid = numbers[start + (end - start) // 2]
        num = mid[:i]
        chr = "0" if comp("0", mid[i]) else "1"
        if end - start % 2 == 0:
            mid2 = numbers[start + (end - start) // 2 + 1]
            dig1 = mid[i]
            dig2 = mid2[i]
            if dig2 != dig1:
                chr = default
        num += chr
        i += 1
        started = False
        for j in range(start, end):
            if not numbers[j].startswith(num):
                if not started:
                    continue
                else:
                    end = j
                    break
            if not started:
                start = j
                started = True
    return numbers[start]


def same(arg1, arg2):
    return arg1 == arg2


def diff(arg1, arg2):
    return arg1 != arg2


def main(example=False):
    og_numbers = list(read_file(example))
    og_numbers.sort()
    co2_numbers = og_numbers[:]
    og = get_number(og_numbers, same, default=1)
    co2 = get_number(co2_numbers, diff, default=0)
    res = convert_binary(og) * convert_binary(co2)
    print(res)
    return res


assert main(True) == 230
main()
