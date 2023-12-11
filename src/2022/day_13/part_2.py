import json

from utils.utils import read_file


def append(res, idx, val):
    for i in idx[:-1]:
        res = res[i]
    assert len(res) == idx[-1]
    res.append(val)


def parse_line(line):
    return json.loads(line)  ## fucking AAAAA
    # line = line[1:-1]
    # res = []
    # idx = [0]
    # in_num = False
    # num = ""
    # for i, char in enumerate(line):
    #     if in_num and char in "[],":
    #         append(res, idx, int(num))
    #         num = ""
    #         in_num = False
    #
    #     if char == "[":
    #         append(res, idx, [])
    #         idx.append(0)
    #     elif char == "]":
    #         idx.pop(-1)
    #     elif char == ",":
    #         idx[-1] += 1
    #     else:
    #         in_num = True
    #         num += char
    # if in_num:
    #     append(res, idx, int(num))
    # return res


def convert_to_list(val):
    if isinstance(val, list):
        return val
    return [val]


def in_order(l, r):
    for i in range(len(l)):
        if i >= len(r):
            return False
        val_l, val_r = l[i], r[i]

        if isinstance(val_l, list) or isinstance(val_r, list):
            is_in_order = in_order(convert_to_list(val_l), convert_to_list(val_r))
            if is_in_order is None:
                continue
            else:
                return is_in_order
        elif val_l == val_r:
            continue
        else:
            return val_l < val_r
    if len(l) < len(r):
        return True


def sort_pairs(pairs, sorted):
    s = 0
    for i in range(len(pairs)):
        pair = pairs[i]
        x = in_order(*pair)
        if x:
            s += i + 1
    return s


def main(example=False):
    pairs = []
    r, l = None, None
    for line in read_file(example):
        if not line:
            pairs.append((r,l))
            r, l = None, None
        elif r is None:
            r = parse_line(line)
        else:
            l = parse_line(line)
    pairs.append((r, l))
    vals = []
    for pair in pairs:
        vals.extend(pair)
    idx_2 = 1
    idx_6 = 2
    for val in vals:
        if in_order(val, [[2]]):
            idx_2 += 1
        if in_order(val, [[6]]):
            idx_6 += 1
        else:
            print(val)
    res = idx_2 * idx_6
    print(res)
    return res


assert main(True) == 140
print(main())
