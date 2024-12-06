from utils.utils import *

directions = [
    go_up,
    go_right,
    go_down,
    go_left
]

def main(example=False):
    grid = []
    spots = set()
    start = None
    for row, line in enumerate(read_file(example)):
        grid.append(line)
        if "^" in line:
            start = (row, line.index("^"))
            spots.add(start)
    loc = start
    dir_i = 0
    try:
        while True:
            next = directions[dir_i](loc)
            if grid[next[0]][next[1]] == "#":
                dir_i = (dir_i + 1) % len(directions)
            else:
                loc = next
                spots.add(loc)
    except Exception:
        pass
    res = len(spots)
    print(res)
    return res


assert main(True) == 41
main()
