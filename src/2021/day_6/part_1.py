import math

from utils.utils import read_file


def iterate(spawn, spawn_days, total_days):
    for _ in range(total_days):
        new_babies = spawn[0]
        for i in range(1, spawn_days + 2):
            spawn[i-1] = spawn[i]
        spawn[spawn_days-1] += new_babies
        spawn[spawn_days+1] = new_babies


def main(example=False):
    total_days = 80
    spawn_days = 7
    spawn = {i: 0 for i in range(7+2)}
    for line in read_file(example):
        for num in line.split(","):
            spawn[int(num)] += 1
    iterate(spawn, spawn_days, total_days)
    res = sum(spawn.values())
    print(res)
    return res


assert main(True) == 5934
main()