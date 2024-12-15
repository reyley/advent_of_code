from utils.utils import *

class Rock:
    def __init__(self, r, c):
        self.r = r
        self.c = c


def move(start, grid, directions):
    cur = start
    for direction in directions:
        new_cur = go_by_arrow(cur, direction)
        rock = None
        while isinstance(grid[new_cur], Rock):
            if rock is None:
                rock = grid[new_cur]
            new_cur = go_by_arrow(new_cur, direction)
        if grid[new_cur] == "#":
            continue
        elif grid[new_cur] == ".":
            if rock:
                grid.add(rock.r, rock.c, ".")
                cur = rock.r, rock.c
                rock.r, rock.c = new_cur
                grid.add(rock.r, rock.c, rock)
            else:
                cur = new_cur


def main(example=False):
    grid = Grid()
    start = None
    rocks = []
    directions = ""
    for r, split_file_line in enumerate(read_split_file(example)):
        line, part = split_file_line
        if part == 1:
            for c, ch in enumerate(line):
                if ch == "@":
                    start = (r,c)
                    grid.add(r, c, ".")
                elif ch == "O":
                    rock = Rock(r,c)
                    rocks.append(rock)
                    grid.add(r,c,rock)
                else:
                    grid.add(r, c, ch)
        if part == 2:
            directions += line

    move(start, grid, directions)
    res = sum(100*rock.r + rock.c for rock in rocks)
    print(res)
    return res


assert main(True) == 10092
main()
