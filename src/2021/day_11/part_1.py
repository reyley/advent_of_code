from utils.utils import read_file


class Octopus:
    def __init__(self, num, key):
        self.num = num
        self.neighbors = []
        self.flashed = False
        self.key = key

    def add_neighbor(self, octo):
        self.neighbors.append(octo)

    def add(self, flashed_octs):
        if not self.flashed:
            self.num += 1
            if self.num == 10:
                self.flash(flashed_octs)

    def flash(self, flashed_octs):
        self.flashed = True
        self.num = 0
        flashed_octs.add_line(self.key)
        for n in self.neighbors:
            n.add_line(flashed_octs)

def add_neighbors(grid):
    for key, oc in grid.items():
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if (i, j) != (0, 0):
                    n_key = key[0] + i, key[1] + j
                    if n_key in grid:
                        oc.add_neighbor(grid[n_key])


def main(example=False):
    grid = dict()
    for i, line in enumerate(read_file(example)):
        for j, num_str in enumerate(line):
            key = (i, j)
            grid[key] = Octopus(int(num_str), key)
    add_neighbors(grid)

    num_flashed = 0
    for _ in range(100):
        flashed_octs = set()
        for oc in grid.values():
            oc.add(flashed_octs)
        num_flashed += len(flashed_octs)
        for key in flashed_octs:
            grid[key].flashed = False

    res = num_flashed
    print(res)
    return res


assert main(True) == 1656
main()
