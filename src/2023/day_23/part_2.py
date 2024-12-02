from utils.utils import *
import heapq

class Path:

    def __init__(self, tile, prev_path=None):
        self.path = {tile.key()} if prev_path is None else prev_path.union({tile.key()})
        self.cur = tile

    def weight(self):
        return -(len(self.path) + Tile.n_rows - self.cur.r + Tile.n_cols - self.cur.c)

    def __lt__(self, other):
        return self.cur.key().__lt__(other.cur.key())

    def __len__(self):
        return len(self.path)

class Tile:
    all = None
    next_func = {
        "v": go_down,
        "^": go_up,
        ">": go_right,
        "<": go_left
    }
    n_rows = 0
    n_cols = 0
    def __init__(self, r, c, char):
        self.r = r
        self.c = c
        self.char = char
        Tile.n_rows = max(self.n_rows, r+1)
        Tile.n_cols = max(self.n_cols, c+1)
        if char != "#":
            self.all[self.key()] = self

    def key(self):
        return self.r, self.c

    def next(self):
        # if self.char == ".":
        options =  traverse_neighbors(self.key())
        # else:
        #     options = [self.next_func[self.char](self.key())]
        return [self.all[x] for x in options if x in self.all]

    def __repr__(self):
        return f"{self.char}({self.key()})"

    @classmethod
    def print(cls, path):
        for r in range(cls.n_rows):
            line = ""
            for c in range(cls.n_cols):
                if (r,c) in path.path:
                    line += "O"
                elif (r,c) in cls.all:
                    line += cls.all[(r,c)].char
                else:
                    line += "#"
            print(line)


    @classmethod
    def longest_path(cls):
        start = Path(Tile.all[(0,1)])
        end = (cls.n_rows - 1, cls.n_cols -2)
        h = []
        heapq.heappush(h,(start.weight(), start))
        result = 0
        while h:
            _, path = heapq.heappop(h)
            options = [x for x in cls.all[path.cur.key()].next() if x.key() not in path.path]
            if len(options) == 2:
                # pass
                Tile.print(path)
                print(options)
            for nxt in options:
                if nxt.key() == end:
                    print(result)
                    result = max(len(path), result)
                new_path = Path(nxt, path.path)
                heapq.heappush(h,(new_path.weight(), new_path))
        return result

def main(example=False):
    Tile.all = {}
    for r,c,char in read_map(example):
        Tile(r,c,char)
    res = Tile.longest_path()
    print(res)
    return res


assert main(True) == 154
main()
