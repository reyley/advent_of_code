from utils.utils import read_file
from collections import deque


def main(example=False):
    d = deque()
    s = 0
    for line in read_file(example):
        num = int(line)
        prev = None
        if len(d) == 3:
            prev = sum(d)
            d.popleft()
        d.append(num)
        if prev is not None and sum(d) > prev:
            s += 1
    res = s
    print(res)
    return res


assert main(True) == 5
main()
