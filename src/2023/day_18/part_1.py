import math

from utils.utils import *

dir_map = {
    "U": go_up,
    "D": go_down,
    "R": go_right,
    "L": go_left
}


def fill_interior(border, min_r, max_r, min_c, max_c):
    start = (1,1)
    interior = {start}
    next_dots = [start]
    while next_dots:
        cur_dot = next_dots.pop(-1)
        for next_dot in traverse_neighbors(cur_dot):
            if next_dot not in border and next_dot not in interior:
                interior.add(next_dot)
                next_dots.append(next_dot)
    return len(interior) + len(border)



def main(example=False):
    cur = (0,0)
    m = {cur}
    ext = set()
    max_r = -math.inf
    min_r = math.inf
    max_c = -math.inf
    min_c = math.inf
    for line in read_file(example):
        direction, number, colour = line.split(" ")
        number = int(number)
        for _ in range(number):
            cur = dir_map[direction](cur)
            print(cur)
            m.add(cur)
            max_r = max(max_r, cur[0])
            max_c = max(max_c, cur[1])
            min_r = min(min_r, cur[0])
            min_c = min(min_c, cur[1])
    for r in range(min_r, max_r + 1):
        line = []
        for c in range(min_c, max_c + 1):
            if (r,c) == (0,0):
                line += "S"
            else:
                line += "#" if (r,c) in m else "."
        print("".join(line))
    res = fill_interior(m, min_r, max_r, min_c, max_c)
    print(res)
    return res


assert main(True) == 62
main()
