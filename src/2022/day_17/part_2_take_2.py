import datetime
from copy import deepcopy
from statistics import mean

from utils.utils import read_file


class Stream:
    def __init__(self, stream):
        self.stream = stream
        self.idx = 0

    def get(self):
        r = self.stream[self.idx]
        self.idx = (self.idx + 1) % len(self.stream)
        if r == '<':
            return [0, -1]
        return [0, 1]

    def cut(self, start=None, end=None, length=None):
        if start is None:
            start = self.idx
        if end is None:
            end = (start + length) % len(self.stream)
        if end > start:
            return self.stream[start:end]
        return self.stream[start:] + self.stream[:end]

    def move(self, n):
        self.idx = (self.idx + n) % len(self.stream)


class Mem:
    def __init__(self):
        self.mem = {}
        self.l = set()

    def add(self, p_h, p_idx, h, idx, stream):
        s = stream.cut(start=p_idx, end=idx)
        self.l.add(len(s))
        self.mem[s] = (h - p_h)

    def check(self, stream):
        for l in self.l:
            s = stream.cut(length=l)
            if s in self.mem:
                return self.mem[s], len(s)
        return None, None

    def print(self):
        for x,y in self.mem.items():
            print(x, y)


def shape_line(line, w):
    return list(line) + ["."]*(w - len(line))


def make_shapes(width):
    return {
        0: [
            shape_line("..@@@@", width)
        ],
        1: [
            shape_line("...@.", width),
            shape_line("..@@@", width),
            shape_line("...@.", width)
        ],
        2: [
            shape_line("..@@@", width),
            shape_line("....@", width),
            shape_line("....@", width)
        ],
        3: [
            shape_line("..@", width),
            shape_line("..@", width),
            shape_line("..@", width),
            shape_line("..@", width)
        ],
        4: [
            shape_line("..@@", width),
            shape_line("..@@", width)
        ]
    }


def shape_loc(t, loc):
    r, c = loc
    if t == 0:
        return [
            loc,
            [r, c + 1],
            [r, c + 2],
            [r, c + 3],
        ]
    if t == 1:
        return [
            [r, c + 1],
            [r - 1, c],
            [r - 1, c + 1],
            [r - 1, c + 2],
            [r - 2, c + 1],
        ]
    if t == 2:
        return [
            [r, c + 2],
            [r - 1, c + 2],
            [r - 2, c],
            [r - 2, c + 1],
            [r - 2, c + 2],
        ]
    if t == 3:
        return [
            [r, c],
            [r - 1, c],
            [r - 2, c],
            [r - 3, c],
        ]
    if t == 4:
        return [
            [r, c],
            [r, c + 1],
            [r - 1, c],
            [r - 1, c + 1],
        ]


def get_height(tower):
    height = len(tower)
    while height > 1 and "@" not in tower[height - 1]:
        height -= 1
    return height


def add_shape(t, tower, width, shapes):
    height = get_height(tower)
    while len(tower) <= height + 3:
        tower.append(["."]*width)
    while len(tower) > height + 3:
        tower.pop(-1)
    tower.extend(deepcopy(shapes[t]))


def move_shape_stream(t, tower, stream, loc):
    locs = shape_loc(t, loc)
    direction = stream.get()
    if try_move(locs, direction, tower):
        move(locs, direction, tower)
        return [loc[0], loc[1] + direction[1]]
    return loc


def try_move(locs, direction, tower):
    for loc in locs:
        new_loc = [loc[0] + direction[0], loc[1] + direction[1]]
        if new_loc in locs:
            continue
        if new_loc[1] < 0:
            return False
        try:
            x = tower[new_loc[0]][new_loc[1]]
            if x == "@":
                return False
        except IndexError:
            return False
    return True


def move(locs, direction, tower):
    for loc in locs:
        tower[loc[0]][loc[1]] = "."
    for loc in locs:
        new_loc = loc[0] + direction[0], loc[1] + direction[1]
        tower[new_loc[0]][new_loc[1]] = "@"


def move_shape_down(t, tower, loc):
    locs = shape_loc(t, loc)
    if try_move(locs, [-1, 0], tower):
        move(locs, [-1, 0], tower)
        return [loc[0] - 1, loc[1]], False
    else:
        return loc, True


def move_shape_to_bottom(t, tower, stream):
    stopped = False
    loc = [-1, 2]
    while not stopped:
        loc = move_shape_stream(t, tower, stream, loc)
        loc, stopped = move_shape_down(t, tower, loc)


def get_tower_hight_after_rocks(n_rocks, width, s:str, mem):
    # mem = Mem()
    stream = Stream(s)
    shapes = make_shapes(width)
    tower = []
    height = 0
    i = 0
    p_h, p_idx = 0, 0
    add_to_mem = False
    while i < n_rocks:
        if i % 5 == 0 and n_rocks - i > 5:
            if add_to_mem:
                h, idx = get_height(tower) + height, stream.idx
                mem.add_line(p_h, p_idx, h, idx, stream)
                add_to_mem = False
            new_height, idx_diff = mem.check(stream)
            if new_height is not None:
                height = get_height(tower) + new_height + height
                i += 5
                stream.move(idx_diff)
                tower = []
                continue
            else:
                add_to_mem = True
                p_h, p_idx = get_height(tower) + height, stream.idx
        if i % 10 == 0:
            # print(i, get_height(tower) + height)
            if len(tower) > 20:
                height += len(tower) - 20
                tower = tower[-20:]
        t = i % len(shapes)
        add_shape(i % len(shapes), tower, width, shapes)
        move_shape_to_bottom(t, tower, stream)
        i += 1
    mem.print()
    return height + get_height(tower)


def print_tower(tower):
    for x in tower[::-1]:
        print("".join(x))
    print("~~~~~~~~~~~~~")


def detect_cycle(diffs, min_len):
    min_len = min(min_len, 697)
    for i in range(min_len, len(diffs)//3):
        x1 = [x[1] for x in diffs[-i:]]
        x2 = [x[1] for x in diffs[-2*i: -i]]
        x3 = [x[1] for x in diffs[-3*i: -2*i]]
        if x2 == x1 and x1 == x3:
            return diffs[-3*i - 1][0], x1
    return None, None


def get_cycle(s):
    dots = {}
    diffs = []
    cycle_start = None
    cycle = None
    cycle_diff = 5
    mem = Mem()
    for x in range(cycle_diff, 1000001, cycle_diff):
        if x % 100 == 0:
            print(f"x: {x}")
        res = get_tower_hight_after_rocks(x, 7, s, mem)
        dots[x] = res
        if len(dots) > 1:
            diffs.append([x, res - dots[x - cycle_diff]])
        if x > (len(s) // 3) and x % 100 == 0:
            cycle_start, cycle = detect_cycle(diffs, len(s) // 10)
        if cycle_start:
            print(cycle_start, len(cycle))
            break
    height_start = dots[cycle_start]
    return cycle_start, height_start, cycle, cycle_diff


def main(example=False):
    s = ""
    for line in read_file(example):
        s = line
        print(len(s))

    # res = get_tower_hight_after_rocks(10000000, 7, s)
    # print(res)
    # return res

    cycle_start, height_start, cycle, cycle_diff = get_cycle(s)
    end = 10**12
    x = (end - cycle_start)//(len(cycle)*cycle_diff)
    cur_height = height_start + x*sum(cycle)
    cur = cycle_start + x*len(cycle)*cycle_diff
    if cur < end:
        for h in cycle:
            cur_height += h
            cur += cycle_diff
            if cur >= end:
                break
    print(cur)
    assert cur == end
    res = cur_height
    print(res)
    return res


assert main(True) == 1514285714288
# print(main())
