import math

from utils.utils import read_file


class Node:
    def __init__(self, loc, ln):
        self.loc = loc
        self.len = ln


def get_next_nodes(node, grid):
    next_nodes = []
    for i_d, j_d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        try:
            i, j = node.loc
            loc = (i + i_d, j + j_d)
            val = grid[loc[0]][loc[1]]
            prev_val = grid[i][j]
            if ord(val) - ord(prev_val) <= 1:
                next_nodes.append(Node(loc, node.len + 1))
        except IndexError:
            continue
    return next_nodes


def traverse(grid, start, end, mem):
    start = Node(start, 0)
    next_nodes = get_next_nodes(start, grid)
    nodes_i = 0
    while nodes_i < len(next_nodes):
        node = next_nodes[nodes_i]
        nodes_i += 1
        if mem.get(node.loc, math.inf) < node.len:
            continue
        if mem.get(end, math.inf) < node.len:
            continue
        if mem.get(node.loc, math.inf) > node.len:
            mem[node.loc] = node.len
            next_nodes.extend(get_next_nodes(node, grid))


def main(example=False):
    start = None
    end = None
    grid = []
    for i, line in enumerate(read_file(example)):
        grid.append(list(line))
        if "S" in line:
            j = line.index("S")
            start = (i, j)
            grid[i][j] = "a"
        if "E" in line:
            j = line.index("E")
            end = (i, j)
            grid[i][j] = "z"

    mem = {start: 1}
    print(start, end)
    traverse(grid, start, end, mem)
    print(mem)
    res = mem[end]
    print(res)
    return res


assert main(True) == 31
print(main())
