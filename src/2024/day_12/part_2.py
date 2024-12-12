from utils.utils import *


class Chunk:
    non_chunked: set = set()
    grid: Grid = None

    def __init__(self):
        self.blocks = set()
        self.corners = 0

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
                    pass
                elif i in self.non_chunked:
                    blocks_to_add.add(i)
            self.corners += self.count_corners(cur, neighbors)
        pass

    def count_corners(self, cur, neighbors):
        corners = 0
        ch = self.grid.get(cur)
        for i in range(4):
            n_1, n_2 = neighbors[i], neighbors[i-1]
            if self.grid.get(n_1) != ch and self.grid.get(n_2) != ch:
                corners += 1
            if self.grid.get(n_1) == self.grid.get(n_2) == ch:
                diagonal = (
                    n_1[0] if n_1[0] != cur[0] else n_2[0],
                    n_1[1] if n_1[1] != cur[1] else n_2[1],
                )
                if self.grid.get(diagonal) != self.grid.get(cur):
                    corners += 1
        return corners


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
    res = sum(chunk.corners * len(chunk.blocks) for chunk in chunks.values())
    print(res)
    return res


assert main(True) == 236
main()
