from utils.utils import *


def main(example=False):
    rows = []
    for line in read_file(example):
        x = line.split()
        x_no_empty = [i for i in x if i != '']
        rows.append(x_no_empty)
    res = 0
    for i in range(len(rows[0])):
        ans = 0
        if rows[-1][i] == "+":
            ans = sum(int(rows[j][i]) for j in range(len(rows)-1))
        elif rows[-1][i] == "*":
            ans = mul(int(rows[j][i]) for j in range(len(rows)-1))
        res += ans
    print(res)
    return res


assert main(True) == 4277556
main()