from utils.utils import *


def main(example=False):
    res = 50
    z_num = 0
    for line in read_file(example):
        RL = line[0]
        num = int(line[1:])
        if RL == "L":
            res -= num
        else:
            res += num
        res = res % 100
        print(res)
        if res == 0:
            z_num = z_num + 1
    res = z_num
    print(res)
    return res


assert main(True) == 3
main()
