import re

from utils.utils import *

pattern = re.compile("mul\((?P<num1>\d{1,3}),(?P<num2>\d{1,3})\)")


def main(example=False):
    res = 0
    for line in read_file(example):
        matches = pattern.findall(line)
        for x,y in matches:
            res += int(x) * int(y)
    print(res)
    return res


assert main(True) == 161
main()
