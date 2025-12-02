from utils.utils import *


def main(example=False):
    res = 50
    z_num = 0
    for line in read_file(example):
        RL = line[0]
        num = int(line[1:])
        prev = res
        if RL == "L":
            res -= num
        else:
            res += num
        new = res
        res = res % 100

        prev_z = z_num
        if new == 0:
            z_num = z_num + 1
        z_num += abs(new//100)
        if new < 0 == res == 0:
            z_num += 1
        if prev == 0 and new < 0:
            z_num -= 1
        print(f"{prev=}, {new=}, dz={z_num - prev_z}")
    res = z_num
    print(res)
    return res


assert main(True) == 6
main()
