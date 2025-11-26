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


def move(seq1, is_numbers=False):
    all_arrows = [""]
    # if not is_numbers:
    #     seq1 = "A" + seq1
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


@cache
def min_seq(char_1, char_2, depth, is_number):
    if depth == 0:
        print(move(char_1 + char_2, False))
        ret_val = len(move(char_1 + char_2, False)[0])
        print(f"{char_1=}, {char_2=}, {depth=}, return={ret_val}")
        return ret_val
    options = move(char_1 + char_2, is_number)
    option_vals = []
    for option in options:
        option_val = 0
        for i in range(len(option) - 1):
            option_val += min_seq(option[i], option[i+1], depth - 1, False)
        option_vals.append(option_val)
    print(f"{char_1=}, {char_2=}, {depth=}, return={min(option_vals)}")
    return min(option_vals)


# @cache
# def min_seq(char_1, char_2):
#     print(char_1, char_2)
#     all_arrows1 = move(char_1 + char_2, True)
#     final_arrows = all_arrows1 if isinstance(all_arrows1,list) else [all_arrows1]
#     min_arr = None
#     for i in range(10):
#         new_final_arrows = []
#
#         for arr1 in final_arrows:
#             new_final_arrows.extend(move(arr1))
#         min_length = min(len(arr) for arr in new_final_arrows)
#         final_arrows = [arr for arr in new_final_arrows if len(arr) == min_length]
#         # if char_1 == "0" and char_2 == "2":
#         print(len(final_arrows))
#     for arr in final_arrows:
#         if min_arr is None:
#             min_arr = arr
#         elif len(arr) < len(min_arr):
#             min_arr = arr
#     print(char_1, char_2, min_arr)
#     return min_arr


def main(example=False):
    res = 0
    for line in read_file(example):
        multiplier = int(line[:-1])
        line = "A" + line
        final_length = 0
        for i in range(len(line) - 1):
            final_length += min_seq(line[i], line[i+1], 2, True)
        res += final_length * multiplier
        # all_arrows1 = move(line, True)
        # final_arrows = all_arrows1
        # for i in range(2):
        #     new_final_arrows = []
        #     for arr1 in final_arrows:
        #         new_final_arrows.extend(move(arr1))
        #     final_arrows = new_final_arrows
        # min_len_3 = min(len(arr) for arr in final_arrows)
        # res += min_len_3* multiplier
        # print(f"{len(arrows3)=}, {line=}, {arrows1=}, {arrows2=}, {arrows3=}")
    print(res)
    return res


assert main(True) == 126384
main()
