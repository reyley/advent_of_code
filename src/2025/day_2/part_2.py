from utils.utils import *

divisors = [2, 3, 5, 6, 7, 10]

def sum_range(r: tuple, n=2):
    start, end = r
    res = 0
    if len(start) == len(end) and len(start)%n != 0:
        return 0
    new_start = start
    if len(start) % n != 0:
        while len(new_start) % n != 0:
            new_start = "1" + "0"*(len(new_start))

    option_pref = new_start[:len(new_start)//n]
    option_num = int(option_pref*n)
    if option_num < int(new_start):
        option_pref = str(int(option_pref) + 1)
        option_num = int(option_pref * n)
    while option_num <= int(end):
        res += option_num
        option_pref = str(int(option_pref) + 1)
        option_num = int(option_pref * n)
    return res

def calc_range(r: tuple):
    res = 0
    for p in divisors:
        if p > len(r[1]):
            break
        sum_r = sum_range(r, p)
        if p == 6 or p == 10:
            res -= sum_r
        else :
            res += sum_r
    return res

def main(example=False):
    ranges = []
    for line in read_file(example):
        ranges_s = line.split(",")
        for r in ranges_s:
            start, end = r.split("-")
            ranges.append((start, end))
    res = 0
    for r in ranges:
        res += calc_range(r)
    print(res)
    return res


assert main(True) == 4174379265
main()