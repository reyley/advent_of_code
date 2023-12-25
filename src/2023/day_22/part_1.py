from collections import defaultdict
from typing import Optional

from utils.utils import *

class Brick:
    map: Optional[dict[tuple,"Brick"]] = None
    start_rows: Optional[defaultdict[int,list["Brick"]]] = None
    bricks = None
    x_range = [0,0]
    y_range = [0,0]
    z_range = [0,0]
    def __init__(self, line):
        self.line = line
        if Brick.start_rows is None:
            Brick.start_rows = defaultdict(list)
        if Brick.bricks is None:
            Brick.bricks = []
        self.id = len(self.bricks)
        corner1, corner2 = line.split("~")
        x1,y1,z1 = int_line(corner1)
        x2,y2,z2 = int_line(corner2)
        self.blocks = set()
        for x in range(x1, x2+1):
            self.x_range[0] = min(self.x_range[0], x)
            self.x_range[1] = max(self.x_range[1], x)
            for y in range(y1, y2+1):
                self.y_range[0] = min(self.y_range[0], y)
                self.y_range[1] = max(self.y_range[1], y)
                for z in range(z1, z2+1):
                    self.blocks.add((x,y,z))
                    self.z_range[0] = min(self.z_range[0], z)
                    self.z_range[1] = max(self.z_range[1], z)
        self.start_rows[z1].append(self)
        self.blocks_bellow = set()
        self.blocks_above = set()
        self.bricks.append(self)

    def __repr__(self):
        return str(self.id)

    def drop(self):
        overlap = False
        moved = False
        while not overlap:
            new_blocks = {(x,y,z-1) for x,y,z in self.blocks}
            for b in new_blocks:
                if b in self.map and self.map[b] != self:
                    overlap = True
                    self.map[b].blocks_above.add(self)
                    self.blocks_bellow.add(self.map[b])
            if -1 in {z for x,y,z in new_blocks}:
                overlap = True
            if not overlap:
                moved = True
                self.blocks = new_blocks

        for b in self.blocks:
            assert b not in self.map or self.map[b] == self
            self.map[b] = self
        return moved

    def is_removable(self):
        for b_above in self.blocks_above:
            if len(b_above.blocks_bellow) == 1:
                assert b_above.blocks_bellow == {self}
                return False
        parents = set()

        for x,y,z in self.blocks:
            if (x,y,z+1) in self.map and self.map[(x,y,z+1)] != self:
                parents.add(self.map[(x,y,z+1)])

        for parent in parents:
            children = set()
            for x, y, z in parent.blocks:
                key = (x, y, z - 1)
                if key in self.map and self.map[key] != parent:
                    children.add(self.map[key])
            if children != parent.blocks_bellow:
                print(parent.id, children, parent.blocks_bellow)
            if len(children) == 1:
                assert False
        return True

    def __hash__(self):
        return hash(self.line)

    @classmethod
    def fall(cls):
        cls.map = dict()
        for z in range(cls.z_range[0], cls.z_range[1] + 1):
            for brick in cls.start_rows[z]:
                brick.drop()
        for brick in cls.bricks:
            assert brick.drop() == False


    @classmethod
    def count_removables(cls):
        n_removable = 0
        print(len(cls.bricks))
        for b in cls.bricks:
            if b.is_removable():
                n_removable += 1
        return n_removable

    @classmethod
    def draw(cls):
        print("\nSTART DRAW\n")
        full_map = [[["...." for _ in range(0, cls.x_range[1] + 1)] for _ in range(0, cls.y_range[1] + 1)] for _ in range(0, cls.z_range[1] + 1)]
        for b in cls.bricks:
            for key in b.blocks:
                x,y,z = key
                value = str(b.id)
                full_map[z][y][x] = "0"*(4 - len(value)) + value
        for i, a in enumerate(full_map[::-1]):
            print(f"Z: {len(full_map) - i - 1}")
            for b in a:
                print("".join(b))


def main(example=False):
    Brick.map: Optional[dict[tuple,"Brick"]] = None
    Brick.start_rows: Optional[defaultdict[int,list["Brick"]]] = None
    Brick.bricks = None
    Brick.x_range = [0,0]
    Brick.y_range = [0,0]
    Brick.z_range = [0,0]
    for line in read_file(example):
        Brick(line)
    Brick.draw()

    Brick.fall()

    Brick.draw()

    res = Brick.count_removables()
    print(res)
    return res


assert main(True) == 5
main()
