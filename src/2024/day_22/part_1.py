from utils.utils import *

@cache
def next_number(num):
    next_num = num * 64
    num = num ^ next_num
    num = num % 16777216
    next_num = num // 32
    num = num ^ next_num
    num = num % 16777216
    next_num = num * 2048
    num = num ^ next_num
    num = num % 16777216
    return num

def next_n_number(original_num, n):
    num = original_num
    for i in range(n):
        num = next_number(num)
    return num

def main(example=False):
    res = 0
    for line in read_file(example):
        num = int(line)
        r = next_n_number(num, 2000)
        print(r)
        res += r
    print(res)
    return res

assert main(True) == 37327623
main()
