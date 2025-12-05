from utils.utils import *


def main(example=False):
    grid = read_grid(example)
    res = 0
    for y in grid.map.keys():
        if grid.get(y) == ".":
            continue
        n = 0
        for x in traverse_neighbors_horizontal(y):
            if grid.get(x) == "@":
                n += 1
        if n < 4:
            res += 1
    print(res)
    return res


assert main(True) == 13
main()