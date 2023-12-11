from utils.utils import read_file


def make_fold(fold, grid):
    axis = fold[0]
    amount = int(fold[1])
    for dot in grid.copy():
        if axis == "x" and dot[0] > amount:
            delta = 2 * (dot[0] - amount)
            new_x = dot[0] - delta
            grid.add_line((new_x, dot[1]))
            grid.remove(dot)
        elif axis == "y" and dot[1] > amount:
            delta = 2 * (dot[1] - amount)
            new_y = dot[1] - delta
            grid.add_line((dot[0], new_y))
            grid.remove(dot)

def print_grid(grid):
    max_x = max(dot[0] for dot in grid) + 1
    max_y = max(dot[1] for dot in grid) + 1
    arrs = [[" "]*max_x for i in range(max_y)]
    for dot in grid:
        arrs[dot[1]][dot[0]] = "@"
    for row in arrs:
        print("".join(row))

def main(example=False):
    folds = []
    grid = set()
    for line in read_file(example):
        if line.startswith("fold along "):
            line = line.replace("fold along ", "")
            folds.append(line.split("="))
        elif line:
            grid.add(tuple(int(i) for i in line.split(",")))
        pass

    for fold in folds:
        make_fold(fold, grid)

    print_grid(grid)
    res = len(grid)
    print(res)
    return res


assert main(True) == 16
main()
