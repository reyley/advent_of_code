from collections import defaultdict

from utils.utils import read_file

num_count = {
    1: 8,
    2: 6,
    3: 8,
    4: 7,
    5: 4,
    6: 9,
    7: 7
}

rev = {v: k for k, v in num_count.items()}

numbers = {
    frozenset({1, 2, 3, 5, 6, 7}): 0,
    frozenset({3, 6}): 1,
    frozenset({1, 3, 4, 5, 7}): 2,
    frozenset({1, 3, 4, 6, 7}): 3,
    frozenset({2, 3, 4, 6}): 4,
    frozenset({1, 2, 4, 6, 7}): 5,
    frozenset({1, 2, 4, 5, 6, 7}): 6,
    frozenset({1, 3, 6}): 7,
    frozenset({1, 2, 3, 4, 5, 6, 7}): 8,
    frozenset({1, 2, 3, 4, 6, 7}): 9,
}

lens = {
    2: 1,
    3: 7,
    4: 4,
    7: 8
}

def translate(known_nums, num_list, other_nums):
    counter = defaultdict(int)
    char_to_digit = dict()
    for num in num_list:
        for char in num:
            counter[char] += 1
    for char in counter:
        char_to_digit[char] = which_digit(char, counter[char], known_nums)

    str_num = ""
    for num in other_nums:
        set_of_digits = frozenset(char_to_digit[char] for char in num)
        str_num += str(numbers[set_of_digits])
    print(str_num)
    return int(str_num)


def which_digit(char, count, known_nums):
    if count == 8:
        return 3 if char in known_nums[1] else 1
    if count == 7:
        return 4 if char in known_nums[4] else 7
    else:
        return rev[count]


def main(example=False):
    s = 0
    for line in read_file(example):
        known_nums = {}
        num_list = line.split(" | ")[0].split(" ")
        other_nums = line.split(" | ")[1].split(" ")
        for n in num_list:
            if len(n) in lens:
                known_nums[lens[len(n)]] = n
        s += translate(known_nums, num_list, other_nums)
    res = s
    print(res)
    return res


assert main(True) == 61229
main()
