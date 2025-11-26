from utils.utils import *

def get_num_coords(number):
    r,c = 0,0
    if number == "A":
        return 0, 2
    if number == "0":
        return 0, 1
    else:
        c = (int(number) + 2) % 3
        r = (int(number) + 2) // 3
    return r,c


def get_arrow_coords(arrow):
    r,c = 0,0
    if arrow == "A":
        return 1, 2
    if arrow == "^":
        return 1, 1
    if arrow == ">":
        return 0,2
    if arrow == "<":
        return 0,0
    if arrow == "v":
        return 0,1
    return r,c


def move_numbers(num1,num2):
    r1,c1 = get_num_coords(num1)
    r2,c2 = get_num_coords(num2)
    all_arrows = [""]
    rdiff = abs(r2 - r1)
    if c2 == 0 and r1 == 0:
        all_arrows[0] += "^" * rdiff if r2 > r1 else "v" * rdiff
        all_arrows[0] += ">" * (c2 - c1) if c2 > c1 else "<" * (c1-c2)
    elif c1 == 0 and r2 == 0:
        all_arrows[0] += ">" * (c2 - c1) if c2 > c1 else "<" * (c1-c2)
        all_arrows[0] += "^" * rdiff if r2 > r1 else "v" * rdiff
    else:
        new_option = all_arrows[0]
        all_arrows[0] += ">" * (c2 - c1) if c2 > c1 else "<" * (c1-c2)
        all_arrows[0] += "^" * rdiff if r2 > r1 else "v" * rdiff
        new_option += "^" * rdiff if r2 > r1 else "v" * rdiff
        new_option += ">" * (c2 - c1) if c2 > c1 else "<" * (c1-c2)
        if new_option != all_arrows[0]:
            all_arrows.append(new_option)
    return [arrows + "A" for arrows in all_arrows]


def move_arrows(arr1,arr2):
    r1,c1 = get_arrow_coords(arr1)
    r2,c2 = get_arrow_coords(arr2)
    all_arrows = [""]
    rdiff = abs(r2 - r1)
    if c2 == 0 and r1 == 1:
        all_arrows[0] += "^" * rdiff if r2 > r1 else "v" * rdiff
        all_arrows[0] += ">" * (c2 - c1) if c2 > c1 else "<" * (c1-c2)
    elif c1 == 0 and r2 == 1:
        all_arrows[0] += ">" * (c2 - c1) if c2 > c1 else "<" * (c1-c2)
        all_arrows[0] += "^" * rdiff if r2 > r1 else "v" * rdiff
    else:
        new_option = all_arrows[0]
        all_arrows[0] += ">" * (c2 - c1) if c2 > c1 else "<" * (c1-c2)
        all_arrows[0] += "^" * rdiff if r2 > r1 else "v" * rdiff
        new_option += "^" * rdiff if r2 > r1 else "v" * rdiff
        new_option += ">" * (c2 - c1) if c2 > c1 else "<" * (c1-c2)
        if new_option != all_arrows[0]:
            all_arrows.append(new_option)
    return [arrows + "A" for arrows in all_arrows]


def move(seq, is_numbers=False):
    seq1 = "A"+seq
    all_arrows = [""]
    for i in range(len(seq1) - 1):
        new_all_arrows = []
        if is_numbers:
            for arrow in all_arrows:
                options = move_numbers(seq1[i], seq1[i+1])
                for opt in options:
                    new_all_arrows.append(arrow + opt)
        else:
            for arrow in all_arrows:
                options = move_arrows(seq1[i], seq1[i+1])
                for opt in options:
                    new_all_arrows.append(arrow + opt)
        all_arrows = new_all_arrows
    return all_arrows


def main(example=False):
    res = 0
    for line in read_file(example):
        multiplier = int(line[:-1])
        all_arrows1 = move(line, True)
        arrows2 = []
        for arr1 in all_arrows1:
            arrows2.extend(move(arr1))
        arrows3 = []
        for arr2 in arrows2:
            arrows3.extend(move(arr2))
        min_len_3 = min(len(arr) for arr in arrows3)
        res += min_len_3* multiplier
        # print(f"{len(arrows3)=}, {line=}, {arrows1=}, {arrows2=}, {arrows3=}")
    print(res)
    return res


assert main(True) == 126384
main()

us = "v<<A>>^AvA^A/v<<A>>^AAv<A<A>>^AAvAA^<A/>Av<A^>AA<A>Av<A<A>>^/AAA/<Av>A^A"
th = "<v<A>>^AvA^A/<vA<AA>>^AAvA<^A>AAvA    /^A<vA>^AA<A>A<v<A>A>^/AAA/vA<^A>A"
th2 = "<A>A       /v<<AA>^AA>               /AvAA^A<vAAA>^A"
us2 = "<A>A       /<AAv<AA>>^               /AvAA^Av<AAA^>A"
th1 = "^A<<^^A>>AvvvA"
us1 = "^A^^<<A>>AvvvA"
