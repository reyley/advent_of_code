from utils.utils import *

class Rock:
    def __init__(self, r, c):
        self.r = r
        self.c = c

    def spot(self):
        return [(self.r,self.c),(self.r,self.c+1)]

    def next_spots(self, direction):
        next_rc = go_by_arrow((self.r, self.c), direction)
        next_spots = []
        for spot in [next_rc,(next_rc[0],next_rc[1]+1)]:
            if spot not in self.spot():
                next_spots.append(spot)
        return next_spots

    def move(self, direction, grid=None):
        next_rc = go_by_arrow((self.r, self.c), direction)
        if grid:
            assert grid[next_rc] in [".", self] and grid[(next_rc[0],next_rc[1]+1)] in [".", self]
            grid.add(self.r, self.c, ".")
            grid.add(self.r, self.c+1, ".")
            grid.add(next_rc[0], next_rc[1] + 1, self)
            grid.add(next_rc[0], next_rc[1], self)
        self.r, self.c = next_rc

    def __str__(self):
        return "O"

    def __repr__(self):
        return f"O ({self.r},{self.c})"

def get_rocks(loc, grid, direction):
    rocks = []
    new_curs = [loc]
    while any(isinstance(grid[_], Rock) for _ in new_curs):
        if any(grid[_] == "#" for _ in new_curs):
            return None
        curs = new_curs
        new_curs = []
        i = 0
        while i < len(curs):
            x = curs[i]
            i += 1
            if isinstance(grid[x], Rock) and (not rocks or grid[x] != rocks[-1]):
                rock = grid[x]
                rocks.append(rock)
                new_curs.extend(rock.next_spots(direction))
    if any(grid[_] == "#" for _ in new_curs):
        return None
    return rocks


def move(start, grid, directions):
    cur = start
    for direction in directions:
        # grid.print(cur)
        new_cur = go_by_arrow(cur, direction)
        rocks = get_rocks(new_cur, grid, direction)
        if rocks is None:
            continue
        for i in range(len(rocks)):
            rocks[-i - 1].move(direction, grid)
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
                c = c*2
                if ch == "@":
                    start = (r,c)
                    grid.add(r, c, ".")
                    grid.add(r, c+1, ".")
                elif ch == "O":
                    rock = Rock(r,c)
                    rocks.append(rock)
                    grid.add(r,c,rock)
                    grid.add(r,c+1,rock)
                else:
                    grid.add(r, c, ch)
                    grid.add(r, c+1, ch)
        if part == 2:
            directions += line

    move(start, grid, directions)
    res = sum(100*rock.r + rock.c for rock in rocks)
    print(res)
    return res


assert main(True) == 9021
main()
