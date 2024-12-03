import re

from utils.utils import *

pattern = re.compile("mul\((?P<num1>\d{1,3}),(?P<num2>\d{1,3})\)|(don't\(\))|(do\(\))")


def main(example=False):
    res = 0
    is_in_add_mode = True
    for line in read_file(example):
        matches = pattern.findall(line)
        for x,y, dont, do in matches:
            if dont:
                is_in_add_mode = False
            elif do:
                is_in_add_mode = True
            elif is_in_add_mode:
                res += int(x) * int(y)
    print(res)
    return res


assert main(True) == 48
main()
