from collections import defaultdict

from utils.utils import read_file

points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

opposite = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

close_to_open = {v:k for k,v in opposite.items()}

def get_points(line):
    line = list(line)
    i = 0
    while i < len(line):
        char = line[i]
        if char in opposite:
            i += 1
        else:
            open_char = close_to_open[char]
            if line[i - 1] == open_char:
                line.pop(i)
                line.pop(i-1)
                i = i - 1
            else:
                return points[char]
    return 0


def main(example=False):
    res = 0
    for line in read_file(example):
        res += get_points(line)
    print(res)
    return res


assert main(True) == 26397
main()
