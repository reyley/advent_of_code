from utils.utils import *


def calc(op, nums):
    if op == "+":
        return sum(nums)
    elif op == "*":
        return mul(nums)

def main(example=False):
    rows = []
    max_len = 0
    for line in read_file_not_strip(example):
        x = line
        rows.append(x)
        max_len = max(max_len, len(x))
    res = 0
    nums = []
    for i in range(max_len - 1, -1,-1):
        num = ""
        for j in range(len(rows)):
            if i >= len(rows[j]) or rows[j][i] == ' ':
                continue
            elif rows[j][i] in "+*":
                res += calc(rows[j][i], [int(num)] + nums)
                num = ""
                nums = []
            else:
                num += rows[j][i]
        if num:
            nums.append(int(num))
    print(res)
    return res


assert main(True) == 3263827
main()