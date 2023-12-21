from utils.utils import *
import queue

class Plot:
    start = None
    map = None

    n_cols = 0
    n_rows = 0

    def __init__(self, r,c,char):
        if char == "#":
            return
        if char == "S":
            Plot.start = self
        self.r = r
        self.c = c
        Plot.n_rows = max(self.n_rows, r)
        Plot.n_cols = max(self.n_cols, c)
        self.map[(r,c)] = self

    def key(self):
        return self.r, self.c

    def get(self, r,c):
        return self.map.get((r %self.n_rows, c %self.n_cols))

    @classmethod
    def has(self, r,c):
        return (r %self.n_rows, c %self.n_cols) in self.map

    @classmethod
    def traverse(cls, n_steps):
        past = set()
        evens = set()
        q = queue.Queue()
        q.put((0, cls.start.key()))
        while not q.empty():
            step, cur = q.get()
            if cur in past:
                continue
            if step % 2 == 0:
                evens.add(cur)
            assert cur not in past
            past.add(cur)
            neighbors = traverse_neighbors(cur)
            for nxt in neighbors:
                # print(neighbors)
                if nxt not in past and cls.has(*nxt) and step < n_steps:
                    q.put((step + 1, nxt))
        cls.plot(evens)
        return len(evens)

    @classmethod
    def plot(cls, steps):
        for r in range(cls.n_rows):
            line = ""
            for c in range(cls.n_cols):
                if (r,c) == cls.start.key():
                    line += "S"
                elif (r,c) in steps:
                    line += "O"
                elif (r,c) in cls.map:
                    line += "."
                else:
                    line += "#"
            print(line)






def main(example=False):
    Plot.map = {}
    for r,c,char in read_map(example):
        Plot(r,c,char)
    res = Plot.traverse(64)
    print(res)
    return res


# assert main(True) == 42
main()
