from utils.utils import *


class Elem:
    def __init__(self, ch):
        self.ch = ch
        self.on_path = ch != "#"
        self.dist_from_start = 0
        self.next = None

    def __eq__(self, other):
        if isinstance(other, Elem):
            return self.ch == other.ch
        else:
            return self.ch == other


def num_shortcuts(cur, step, grid, length, speedup=100):
    total_num = 0
    step_elem = grid.get(step)
    cur_elem: Elem = grid.get(cur)
    init_length = cur_elem.dist_from_start
    if step_elem and not step_elem.on_path:
        steps_2 = traverse_next_neighbors(step, cur)
        for step_2 in steps_2:
            step_2_elem: Elem = grid.get(step_2)
            if step != step_2 and step_2_elem:
                if step_2_elem.on_path:
                    if step_2_elem.dist_from_start - init_length >= speedup + 2:
                        total_num += 1
    return total_num


def find_paths(grid, length, speedup=100):
    prev = None
    cur = grid.start
    total_num = 0
    while cur != grid.end:
        cur_elem = grid.get(cur)
        if length - cur_elem.dist_from_start < speedup:
            break
        steps = traverse_next_neighbors(cur, prev)
        for step in steps:
            total_num += num_shortcuts(cur, step, grid, length, speedup)

        prev = cur
        cur = cur_elem.next
    return total_num

def initial_traverse(grid):
    prev = None
    cur = grid.start
    length = 0
    while cur != grid.end:
        next_step = None
        steps = traverse_next_neighbors(cur, prev)
        length += 1
        for step in steps:
            if step != prev and grid.get(step).on_path:
                assert next_step is None
                next_step = step
                grid[next_step].dist_from_start = length
                grid[cur].next = next_step
        prev = cur
        cur = next_step
    return length


def main(example=False):
    grid = Grid(start_ch="S", end_ch="E", elem_class=Elem)
    for r,c,ch in read_map(example):
        grid.add(r,c,ch)
    length = initial_traverse(grid)
    speedup = 10 if example else 100
    res = find_paths(grid, length, speedup)
    print(res)
    return res


assert main(True) == 10
main()
