from collections import defaultdict

from utils.utils import read_file

points = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
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
                return None
    cur_points = 0
    print(line)
    for char in line[::-1]:
        cur_points *= 5
        cur_points += points[opposite[char]]
    print(cur_points)
    return cur_points


def main(example=False):
    points_list = []
    for line in read_file(example):
        p = get_points(line)
        if p is not None:
            points_list.append(p)
    points_list.sort()

    res = points_list[len(points_list)//2]
    print(res)
    return res


assert main(True) == 288957
main()
