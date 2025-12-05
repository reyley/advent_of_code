from utils.utils import *

def remove_rolls(grid):
    removed = 0
    for y in grid.map.keys():
        if grid.get(y) == ".":
            continue
        n = 0
        for x in traverse_neighbors_horizontal(y):
            if grid.get(x) == "@":
                n += 1
        if n < 4:
            removed += 1
            grid.add(y, ch=".")
    return removed

def main(example=False):
    grid = read_grid(example)
    res = 0
    n = remove_rolls(grid)
    while n > 0:
        print(n)
        res += n
        n = remove_rolls(grid)
    print(res)
    return res


assert main(True) == 43
main()