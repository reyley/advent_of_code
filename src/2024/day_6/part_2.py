from collections import defaultdict

from utils.utils import *

class Direction:

    def __init__(self, f, ch):
        self.move = f
        self.ch = ch
        self.next = None
        self.opposite = None

    def set(self, opposite_dir, next_dir):
        self.opposite = opposite_dir
        self.next = next_dir


Direction.up = Direction(go_up, "^")
Direction.right = Direction(go_right, ">")
Direction.down = Direction(go_down, "v")
Direction.left = Direction(go_left, "<")
Direction.up.set(Direction.down, Direction.right)
Direction.right.set(Direction.left, Direction.down)
Direction.down.set(Direction.up, Direction.left)
Direction.left.set(Direction.right, Direction.up)

class Spot:
    grid = None
    def __init__(self, loc, direction):
        self.loc = loc
        self.direction = direction

    def next(self, block=None):
        try:
            next_loc = self.direction.move(self.loc)
            next_direction = self.direction.next
            if next_loc == block or self.get(next_loc) == "#":
                return Spot(self.loc, next_direction)
            else:
                return Spot(next_loc, self.direction)
        except:
            return None

    def get(self, loc):
        return self.grid[loc[0]][loc[1]]

    def h(self):
        return (self.loc, self.direction.ch)

    def __eq__(self, other):
        return self.loc == other.loc and self.direction.ch == other.direction.ch

    def __repr__(self):
        return f"{self.loc} {self.direction.ch}"


def traverse(cur: Spot, block, blocks):
    path = set(cur.h())
    while True:
        next_spot = cur.next(block)
        if next_spot is None:
            break
        if next_spot.h() in path:
            if block is not None:
                blocks.add(block)
            break
        path.add(next_spot.h())
        cur = next_spot
    return path


def main(example=False):
    Spot.grid = []
    start = None
    for row, line in enumerate(read_file(example)):
        Spot.grid.append(line)
        if "^" in line:
            start_loc = (row, line.index("^"))
            start = Spot(start_loc, Direction.up)

    path = traverse(start, None, None)
    potential_blocks = set(s[0] for s in path if s[0] != start.loc)
    blocks = set()
    for i, b in enumerate(potential_blocks):
        print(i)
        traverse(start, b, blocks)
    res = len(blocks)
    print(res)
    return res


assert main(True) == 6
main()
