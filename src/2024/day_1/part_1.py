from utils.utils import *


def main(example=False):
    list_1 = []
    list_2 = []
    for line in read_file(example):
        num_1, num_2 = line.split("  ")
        list_1.append(int(num_1))
        list_2.append(int(num_2))
    list_1.sort()
    list_2.sort()
    res = 0
    for i, j in zip(list_1, list_2):
        res += abs(i - j)
    print(res)
    return res


assert main(True) == 11
main()
