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

def damaged_num_str(damaged_num):
    s_d = []
    if not damaged_num:
        return s_d
    for d in damaged_num:
        s_d.extend(["#"] * d + ["."])
    s_d.pop(-1)
    return s_d

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
        # for x in val:
        #     assert "?" not in val
        #     # print(x, springs, damaged_num)
        #     # print(val, springs, damaged_num)
        #     for i, ch in enumerate(springs):
        #         assert x[i] == ch or ch == "?"
        mem[key] = val
    return val

def is_valid(springs, damaged_num):
    s_d = damaged_num_str(damaged_num)
    s = remove_dots(springs)
    return s == s_d

def progress_to_q(springs, damaged_num):
    s_i = 0
    d_i = 0
    d = None
    d_num = None
    q_i = springs.index("?")
    while s_i < q_i:
        if springs[s_i] == ".":
            if d is None:
                s_i += 1
                continue
            if d == d_num:
                d = None
                d_num = None
                d_i += 1
                s_i += 1
                continue
            if d_num < d:
                return s_i, q_i, d_i, d, d_num, 0
        if springs[s_i] == "#":
            if d_i == len(damaged_num):
                return s_i, q_i, d_i, d, d_num, 0
            elif d is None and d_num is None:
                d = damaged_num[d_i]
                d_num = 1
            elif d == d_num:
                return s_i, q_i, d_i, d, d_num, 0
            elif d_num < d:
                d_num += 1
            s_i += 1
            continue
    return s_i, q_i, d_i, d, d_num, None

def springs_options_inner(springs, damaged_num, mem):
    if not springs and not damaged_num:
        return 1
    if not springs and damaged_num:
        return 0
    if sum(damaged_num) + len(damaged_num) - 1 > len(springs):
        return 0
    if "?" not in springs:
        return 1 if is_valid(springs, damaged_num) else 0
    if damaged_num == []:
        return 1 if "#" not in springs else 0
    s_i, q_i, d_i, d, d_num, num_res = progress_to_q(springs, damaged_num)
    if num_res is not None:
        return num_res
    if d is None and d_num is None:
        # we are at start or after a dot etc
        no_fill_num = springs_options(springs[q_i + 1:], damaged_num[d_i:], mem)
        fill_num = 0
        if d_i >= len(damaged_num):
            return no_fill_num
        d = damaged_num[d_i]
        next_chunk = springs[q_i:q_i+d+1]
        if len(next_chunk) < d:
            fill_num = 0
        elif len(next_chunk) == d:
            if "." in next_chunk or d_i < len(damaged_num) - 1:
                fill_num = 0
            elif d_i == len(damaged_num) - 1:
                fill_num = 1
        elif len(next_chunk) == d + 1:
            if "." in next_chunk[:d] or next_chunk[-1] == "#":
                fill_num = 0
            elif q_i + d + 1 < len(springs):
                fill_num = springs_options(springs[q_i + d + 1:], damaged_num[d_i+1:], mem)
            elif d_i == len(damaged_num) - 1:
                assert q_i + d + 1 == len(springs)
                fill_num = 1
            else:
                # there is not more string left but still more damaged
                fill_num = 0
        return no_fill_num + fill_num
    elif d == d_num:
        # we are at the end of part
        return springs_options(springs[q_i + 1:], damaged_num[d_i + 1:], mem)
    elif d_num < d:
        # we are in the middle of a part
        fill_num = 0
        d = d - d_num
        next_chunk = springs[q_i:q_i+d+1]
        if len(next_chunk) < d:
            fill_num = 0
        elif len(next_chunk) == d:
            if "." in next_chunk or d_i < len(damaged_num) - 1:
                fill_num = 0
            elif d_i == len(damaged_num) - 1:
                fill_num = 1
        elif len(next_chunk) == d + 1:
            if "." in next_chunk[:d] or next_chunk[-1] == "#":
                fill_num = 0
            elif q_i + d + 1 < len(springs):
                fill_num = springs_options(springs[q_i + d + 1:], damaged_num[d_i+1:], mem)
            elif d_i == len(damaged_num) - 1:
                assert q_i + d + 1 == len(springs)
                fill_num = 1
            else:
                # there is not more string left but still more damaged
                fill_num = 0
        return fill_num
    assert d_num is None or d_num <= d
    assert False
    return 0



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
    print(springs, damaged_num)
    if sum(damaged_num) + len(damaged_num) - 1 == len(springs):
        return 1
    springs = remove_dots(list(springs))
    if sum(damaged_num) + len(damaged_num) - 1 >= len(springs):
        return 1
    opt = springs_options(springs, damaged_num)
    print(opt)
    # if len(opt) == 0:
    #     print(springs, damaged_num)
    # for _ in opt:
    #     print(_)
    return opt


def main(example=False):
    res = 0
    for line in read_file(example):
        springs, damaged_num = line.split(" ")
        springs = [springs]*5
        springs = "?".join(springs)
        damaged_num = int_line(damaged_num)
        damaged_num = damaged_num * 5
        opt = count_options(springs, damaged_num)
        # print(springs, damaged_num, opt)
        res += opt
    print(res)
    return res


if __name__ == "__main__":
    assert main(True) == 525152
    main()
