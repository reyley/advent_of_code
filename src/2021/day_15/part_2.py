from utils.utils import read_file
import heapq


class Path:
    def __init__(self, grid):
        self.path = {(0, 0)}
        self.score = 0
        self.grid = grid

    def add(self, i):
        if i in self.path:
            return False
        self.path.add(i)
        self.score += self.grid[i]
        return True


def find_path(grid, end):
    paths = []
    location = (0, 0)
    nodes_traveled = {(0, 0)}
    score = 0
    while True:
        for d_i, d_j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_loc = location[0] + d_i, location[1] + d_j
            if new_loc == end:
                score += grid[end]
                return score
            if new_loc in grid and new_loc not in nodes_traveled:
                new_score = score + grid[new_loc]
                heapq.heappush(paths, (new_score, new_loc))
                nodes_traveled.add(new_loc)
        score, location = heapq.heappop(paths)


def main(example=False):
    grid = {}
    i, j = 0, 0
    for i, line in enumerate(read_file(example)):
        for j, n in enumerate(line):
            grid[(i, j)] = int(n)
    size = i + 1
    for i_i in range(size):
        for k in range(5):
            for j_j in range(size):
                for l in range(5):
                    n = (grid[(i_i, j_j)] + k + l)
                    if n > 9:
                        n = 1 + (n-1)%9
                    i = i_i + size * k
                    j = j_j + size * l
                    grid[(i, j)] = n



    res = find_path(grid, (i, j))
    for i in range(size*5):
        print(" ".join([str(grid[i, j]) for j in range(size*5)]))
    print(res)
    return res


assert main(True) == 315
main()
