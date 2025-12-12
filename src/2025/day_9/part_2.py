from bisect import bisect_left

from utils.utils import *


def is_empty_box(dot1, dot2, x_lines, y_lines):
    start_x = min(dot1[0], dot2[0]) + 1
    end_x = max(dot1[0], dot2[0]) - 1
    start_y = min(dot1[1], dot2[1]) + 1
    end_y = max(dot1[1], dot2[1]) - 1
    x_idx = bisect_left(x_lines, start_x, key=lambda x: x[0][0])
    y_idx = bisect_left(y_lines, start_y, key=lambda x: x[0][1])
    while x_idx < len(x_lines) and x_lines[x_idx][0][0] <= end_x:
        ys = sorted([x_lines[x_idx][0][1], x_lines[x_idx][1][1]])
        if ys[1] < start_y or ys[0] > end_y:
            x_idx += 1
            continue
        else:
            return False
    while y_idx < len(y_lines) and y_lines[y_idx][0][1] <= end_y:
        xs = sorted([y_lines[x_idx][0][0], y_lines[x_idx][1][0]])
        if xs[1] < start_x or xs[0] > end_x:
            y_idx += 1
            continue
        else:
            return False
    return True

def is_inside(dot, dot1, dot2):

def add_line(line, x_lines, y_lines):
    if line[0][0] == line[1][0]:
        x_lines.append(line)
    elif line[0][1] == line[1][1]:
        y_lines.append(line)

def main(example=False):
    x_dots = []
    x_lines = []
    y_lines = []
    prev_dot = None
    first_dot = None
    for line in read_file(example):
        x_dots.append(int_line(line))
        if prev_dot:
            add_line((prev_dot, x_dots[-1]), x_lines, y_lines)
        else:
            first_dot = x_dots[-1]
        prev_dot = x_dots[-1]
    add_line((prev_dot, first_dot), x_lines, y_lines)
    x_dots.sort()
    y_lines.sort(key=lambda x: x[0][1])
    x_lines.sort(key=lambda x: x[0][0])
    max_box_size = 0
    for i in range(len(x_dots)):
        for j in range(i+1, len(x_dots)):
            dot1, dot2 = x_dots[i], x_dots[j]
            box_size = (abs(dot2[0]-dot1[0]) + 1) * (abs(dot2[1]-dot1[1]) + 1)
            if box_size > max_box_size and is_empty_box(dot1, dot2, x_lines, y_lines):
                print(f"New max box found between {dot1} and {dot2} with size {box_size}")
                max_box_size = box_size
    res = max_box_size
    print(res)
    return res


assert main(True) == 24
main()