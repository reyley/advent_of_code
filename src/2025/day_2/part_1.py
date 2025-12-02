from utils.utils import *

def sum_range(r: tuple):
    start, end = r
    res = 0
    if len(start) == len(end) and len(start)%2 == 1:
        return 0
    if len(start) % 2 == 1:
        start = "1" + "0"*len(start)
    option_pref = start[:len(start)//2]
    option_num = int(option_pref*2)
    if option_num < int(start):
        option_pref = str(int(option_pref) + 1)
        option_num = int(option_pref * 2)
    while option_num <= int(end):
        res += option_num
        option_pref = str(int(option_pref) + 1)
        option_num = int(option_pref * 2)
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
        res += sum_range(r)
    print(res)
    return res


assert main(True) == 1227775554
main()