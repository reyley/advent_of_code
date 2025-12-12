from bisect import bisect_left

from utils.utils import *


def main(example=False):
    x_dots = []
    for line in read_file(example):
        x_dots.append(int_line(line))
    x_dots.sort()
    y_dots = sorted(x_dots, key=lambda x: (x[1],x[0]))
    max_box_size = 0
    for i in range(len(x_dots)):
        for j in range(i+1, len(x_dots)):
            dot1, dot2 = x_dots[i], x_dots[j]
            box_size = (abs(dot2[0]-dot1[0]) + 1) * (abs(dot2[1]-dot1[1]) + 1)
            if box_size > max_box_size:
                max_box_size = box_size
    res = max_box_size
    print(res)
    return res


assert main(True) == 50
main()