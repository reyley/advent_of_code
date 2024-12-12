from utils.utils import *


class Chunk:
    non_chunked: set = set()
    grid: Grid = None

    def __init__(self):
        self.blocks = set()
        self.edges = 0

    def add(self, x):
        blocks_to_add = {x}
        while blocks_to_add:
            cur = blocks_to_add.pop()
            neighbors = traverse_neighbors(cur)
            self.blocks.add(cur)
            if cur != x:
                self.non_chunked.remove(cur)
            for i in neighbors:
                if self.grid.get(i) != self.grid.get(x):
                    self.edges += 1
                elif i in self.non_chunked:
                    blocks_to_add.add(i)


def get_chunks(grid):
    chunks = defaultdict(Chunk)
    Chunk.non_chunked = set(grid.map.keys())
    Chunk.grid = grid
    i = 0
    while Chunk.non_chunked:
        cur = Chunk.non_chunked.pop()
        chunks[i].add(cur)
        i += 1
    return chunks


def main(example=False):
    grid = Grid()
    for r,c,ch in read_map(example):
        grid.add(r,c,ch)
    chunks = get_chunks(grid)
    res = sum(chunk.edges * len(chunk.blocks) for chunk in chunks.values())
    print(res)
    return res


assert main(True) == 1930
main()
