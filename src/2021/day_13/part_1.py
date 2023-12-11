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

    make_fold(folds[0], grid)
    res = len(grid)
    print(res)
    return res


assert main(True) == 17
main()
