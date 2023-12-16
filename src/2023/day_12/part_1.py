from utils.utils import read_file, int_line

def get_all_options(num):
    if num == 0:
        return []
    options = [["#"], ["."]]
    for i in range(num - 1):
        new_options = []
        for o in options:
            new_options.append(["#"] + o)
            new_options.append(["."] + o)
        options = new_options
    return options

def springs_options(springs, damaged_num, mem=None):
    if mem is None:
        mem = {}
    if isinstance(springs, str):
        springs = list(springs)
    key = (tuple(springs), tuple(damaged_num))
    if key in mem:
        return mem[key]
    else:
        val = springs_options_inner(springs, damaged_num, mem)
        for x in val:
            assert "?" not in val
            # print(x, springs, damaged_num)
            # print(val, springs, damaged_num)
            for i, ch in enumerate(springs):
                assert x[i] == ch or ch == "?"
        mem[key] = val
    return val

def is_valid(springs, s_d):
    s = remove_dots(springs)
    return s == s_d


def springs_options_inner(springs, damaged_num, mem):
    num = springs.count("?")
    opts = get_all_options(num)
    s_d = []
    for d in damaged_num:
        s_d.extend(["#"] * d + ["."])
    s_d.pop(-1)
    output = []
    for opt in opts:
        s = springs.copy()
        j = 0
        for i, ch in enumerate(s):
            if ch == "?":
                s[i] = opt[j]
                j+= 1
        if is_valid(s, s_d):
            output.append(s)
    return output



def remove_dots(springs):
    new_springs = []
    for i in range(len(springs)):
        if springs[i] == "." and (not new_springs or new_springs[-1] == "."):
            continue
        new_springs.append(springs[i])
    if new_springs and new_springs[-1] == ".":
        new_springs.pop(-1)
    return new_springs

def count_options(springs, damaged_num):
    if sum(damaged_num) + len(damaged_num) - 1 == len(springs):
        return 1
    springs = remove_dots(list(springs))
    if sum(damaged_num) + len(damaged_num) - 1 >= len(springs):
        return 1
    opt = springs_options(springs, damaged_num)
    # if len(opt) == 0:
    #     print(springs, damaged_num)
    # for _ in opt:
    #     print(_)
    return len(opt)


def main(example=False):
    res = 0
    for line in read_file(example):
        springs, damaged_num = line.split(" ")
        damaged_num = int_line(damaged_num)
        opt = count_options(springs, damaged_num)
        # print(springs, damaged_num, opt)
        res += opt
    print(res)
    return res


if __name__ == "__main__":
    assert main(True) == 21
    main()
