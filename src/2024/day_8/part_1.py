from utils.utils import *

class Grid:
    n_rows = 0
    n_cols = 0

    @classmethod
    def print(cls, nodes, ant):
        for r in range(cls.n_rows):
            row = ""
            for c in range(cls.n_cols):
                row += "#" if (r,c) in nodes else "O" if (r,c) in ant else "."
            print(row)


def in_grid(x):
    if x[0] < 0 or x[0] >= Grid.n_rows:
        return False
    if x[1] < 0 or x[1] >= Grid.n_cols:
        return False
    return True


def add(x,y):
    return (x[0] + y[0], x[1] + y[1])


def get_nodes_pair(x, y):
    nodes = set()
    diff_x = (x[0] - y[0], x[1] - y[1])
    diff_y = (y[0] - x[0], y[1] - x[1])
    node = add(x, diff_x)
    if in_grid(node):
        nodes.add(node)
        node = add(node, diff_x)
    node = add(y, diff_y)
    if in_grid(node):
        nodes.add(node)
        node = add(node, diff_y)
    # print(Grid.print(nodes, [x,y]))
    return nodes


def get_nodes_in_list(a_list):
    nodes = set()
    for i, a in enumerate(a_list):
        for j in range(i + 1, len(a_list)):
            nodes.update(get_nodes_pair(a, a_list[j]))
    return nodes


def get_nodes(antenas):
    nodes = set()
    for ch, a_list in antenas.items():
        nodes.update(get_nodes_in_list(a_list))
    return nodes


def main(example=False):
    antenas = defaultdict(list)
    for r, c, char in read_map(example):
        Grid.n_rows = max(Grid.n_rows, r + 1)
        Grid.n_cols = max(Grid.n_cols, c + 1)
        if char != ".":
            antenas[char].append((r, c))
    nodes = get_nodes(antenas)
    res = len(nodes)
    print(res)
    return res


assert main(True) == 14
main()
