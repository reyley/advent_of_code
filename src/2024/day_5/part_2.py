from functools import cmp_to_key

from utils.utils import *


def middle_page(manual, rules):
    is_good = True
    for i in range(len(manual)):
        for j in range(i + 1, len(manual)):
            if f"{manual[j]}|{manual[i]}" in rules:
                is_good = False
    if is_good:
        return 0

    def comp(num1,num2):
        if f"{num1}|{num2}" in rules:
            return -1
        elif f"{num2}|{num1}" in rules:
            return 1
        return 0

    manual = sorted(manual, key=cmp_to_key(comp))

    assert len(manual) % 2 == 1
    return manual[(len(manual)-1)//2]


def main(example=False):
    rules = set()
    manuals = []
    for line, part in read_split_file(example):
        if part == 1:
            rules.add(line)
        elif part == 2:
            manuals.append(int_line(line, delim=","))
    res = 0
    for manual in manuals:
        res += middle_page(manual, rules)
    print(res)
    return res


assert main(True) == 123
main()
