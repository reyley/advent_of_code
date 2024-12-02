from collections import Counter

from utils.utils import *


def main(example=False):
    list_1 = []
    list_2 = []
    for line in read_file(example):
        num_1, num_2 = line.split("  ")
        list_1.append(int(num_1))
        list_2.append(int(num_2))
    counter = Counter(list_2)
    res = 0
    for num in list_1:
        res += num * counter[num]
    print(res)
    return res


assert main(True) == 31
main()
