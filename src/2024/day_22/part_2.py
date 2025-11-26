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
    seq = {}
    seq_i = []
    num = original_num
    for i in range(n):
        next_num = next_number(num)
        seq_i.append(next_num % 10 - num % 10)
        num = next_num
        if i >= 3:
            quad = (seq_i[i-3], seq_i[i-2], seq_i[i-1], seq_i[i])
            if quad not in seq:
                seq[quad] = num % 10
    return seq


def check_seqs(quad, seqs: list[dict], c):
    if quad in c:
        return c[quad]
    res = 0
    for seq in seqs:
        if quad in seq:
            res += seq[quad]
    c[quad] = res
    return res


def main(example=False):
    res = 0
    seqs = []
    c = {}
    for line in read_file(example):
        num = int(line)
        seq = next_n_number(num, 2000)
        seqs.append(seq)
    for seq in seqs:
        for quad in seq:
            r = check_seqs(quad, seqs, c)
            if r > res:
                res = r
                print(res)
                print(quad)
    print(res)
    return res

assert main(True) == 23
main()
