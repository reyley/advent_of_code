from utils.utils import *


def middle_page(manual, rules):
    for i in range(len(manual)):
        for j in range(i + 1, len(manual)):
            if f"{manual[j]}|{manual[i]}" in rules:
                return 0
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


assert main(True) == 143
main()
