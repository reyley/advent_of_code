from utils.utils import read_file

def is_up(prev, cur):
    return prev[0] < cur[0]

def is_down(prev, cur):
    return prev[0] > cur[0]

def is_left(prev, cur):
    return prev[1] > cur[1]

def is_right(prev, cur):
    return prev[1] < cur[1]

def go_up(cur):
    return cur[0] - 1, cur[1]

def go_down(cur):
    return cur[0] + 1, cur[1]

def go_left(cur):
    return cur[0], cur[1] + 1

def go_right(cur):
    return cur[0], cur[1] - 1

def find_next(prev, cur, cur_char):
    if cur_char == ".":
        if is_up(prev, cur):
            return [go_down(cur)]
        if is_down(prev, cur):
            return [go_up(cur)]
        if is_left(prev, cur):
            return [go_right(cur)]
        if is_right(prev, cur):
            return [go_left(cur)]
    if cur_char == "|":
        if is_up(prev, cur):
            return [go_down(cur)]
        if is_down(prev, cur):
            return [go_up(cur)]
        else:
            return [go_up(cur), go_down(cur)]
    if cur_char == "-":
        if is_left(prev, cur):
            return [go_right(cur)]
        if is_right(prev, cur):
            return [go_left(cur)]
        else:
            return [go_right(cur), go_left(cur)]
    if cur_char == "/":
        if is_up(prev, cur):
            return [go_right(cur)]
        if is_right(prev, cur):
            return [go_up(cur)]
        if is_down(prev, cur):
            return [go_left(cur)]
        if is_left(prev, cur):
            return [go_down(cur)]
    if cur_char == "\\":
        if is_down(prev, cur):
            return [go_right(cur)]
        if is_right(prev, cur):
            return [go_down(cur)]
        if is_up(prev, cur):
            return [go_left(cur)]
        if is_left(prev, cur):
            return [go_up(cur)]
    assert False

class Tile:
    all = {}
    def __init__(self, r, c, ch):
        self.r = r
        self.c = c
        self.ch = ch
        self.lit = False
        self.prev = set()
        self.all[(r,c)] = self

    def has_been_here(self, r,c):
        return (r,c) in self.prev

    def next(self, r,c):
        if (r,c) in self.prev:
            return []
        self.prev.add((r,c))
        self.lit = True
        return find_next((r,c), (self.r, self.c), self.ch)

    @classmethod
    def reset(cls):
        for t in cls.all.values():
            t.lit = False
            t.prev = set()

def count_energy(options):
    while options:
        next_step = options.pop(-1)
        tile = next_step[0]
        r,c = next_step[1]
        res = tile.next(r,c)
        for nxt in res:
            if nxt in Tile.all:
                options.append((Tile.all[nxt], (tile.r,tile.c)))
    s = 0
    for t in Tile.all.values():
        if t.lit:
            s += 1
    Tile.reset()
    return s

def main(example=False):
    for r, line in enumerate(read_file(example)):
        n_rows = r + 1
        n_cols = len(line)
        for c, ch in enumerate(line):
            Tile(r,c,ch)

    mx = 0
    for i in range(n_rows):
        options = [(Tile.all[(i,0)], (i,-1))]
        mx = max(count_energy(options), mx)
    for i in range(n_rows):
        options = [(Tile.all[(i,n_cols - 1)], (i,n_cols))]
        mx = max(count_energy(options), mx)
    for i in range(n_cols):
        options = [(Tile.all[(n_rows - 1,i)], (n_rows,i))]
        mx = max(count_energy(options), mx)
    for i in range(n_cols):
        options = [(Tile.all[(0,i)], (-1,i))]
        mx = max(count_energy(options), mx)

    res = mx
    print(res)
    return res


assert main(True) == 51
main()
