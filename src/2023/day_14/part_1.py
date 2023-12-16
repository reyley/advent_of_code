from utils.utils import read_file
from collections import defaultdict

class Rock:
    num_rows = None
    def __init__(self, r, c, char):
        self.r = r
        self.c = c
        self.is_cube = char == "#"
        self.char = char

    def weight(self):
        if self.is_cube:
            return 0
        return self.num_rows - self.r

    def __hash__(self):
        return hash((self.r, self.c))

    def __eq__(self, other):
        return hash(other) == hash(self)

    def __repr__(self):
        return f"{self.char}({self.r}, {self.c})"

    def move_north(self, rocks):
        while (self.r - 1, self.c) not in rocks and self.r > 0:
            self.r -= 1

def main(example=False):
    rocks_by_row = {} # row: columns
    all_rocks = set()
    for r, line in enumerate(read_file(example)):
        rocks_by_row[r] = []
        for c, char in enumerate(line):
            if char != ".":
                rock = Rock(r,c,char)
                all_rocks.add(rock)
                if not rock.is_cube:
                    rocks_by_row[r].append(rock)
    Rock.num_rows = len(rocks_by_row)
    res = 0
    for i in range(len(rocks_by_row)):
        for rock in rocks_by_row[i]:
            all_rocks.remove(rock)
            rock.move_north(all_rocks)
            all_rocks.add(rock)
            res += rock.weight()
    print(res)
    return res


assert main(True) == 136
main()
