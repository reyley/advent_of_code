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


def traverse_shortcuts(cur, prev, depth, start, prev_cheats, grid, init_length, speedup, mem):
    total_num = 0
    if depth == 21:
        return 0
    steps_i = traverse_next_neighbors(cur, prev)
    for step_i in steps_i:
        if (start, step_i) in prev_cheats:
            continue
        step_i_elem: Elem = grid.get(step_i)
        if step_i_elem and step_i_elem.on_path:
            if step_i_elem.dist_from_start - init_length >= speedup + depth:
                total_num += 1
                prev_cheats.add((start, step_i))
        else:
            total_num += traverse_shortcuts(step_i, cur, depth + 1, start, prev_cheats, grid, init_length, speedup, mem)
    return total_num


def num_shortcuts(cur, step, grid, speedup=100):
    mem = {}
    start = cur
    total_num = 0
    step_elem = grid.get(step)
    cur_elem: Elem = grid.get(cur)
    init_length = cur_elem.dist_from_start
    prev_cheats = set()
    if step_elem and not step_elem.on_path:
        prev,cur = cur,step
        total_num = traverse_shortcuts(cur, prev, 2, start, prev_cheats, grid, init_length, speedup, mem)
    return total_num


def find_paths(grid, length, speedup=100):
    prev = None
    cur = grid.start
    total_num = 0
    while cur != grid.end:
        # r,c = cur
        # cur_elem = grid.get(cur)
        # # print(cur)
        # if length - cur_elem.dist_from_start < speedup:
        #     break
        # for i in range(0,21):
        #     for j in range(0,21-i):
        #         if i + j == 0:
        #             continue
        #         if i + j == 1:
        #
        #         for step in [(r + i, c + j), (r + i, c - j), (r - i, c + j), (r - i, c - j)]:
        #             step_elem: Elem = grid.get(step)
        #             if step_elem and step_elem.on_path:
        #                 if step_elem.dist_from_start - cur_elem.dist_from_start >= speedup + i+j:
        #                     print(cur,step)
        #                     total_num += 1
        cur_elem = grid.get(cur)
        print(cur)
        if length - cur_elem.dist_from_start < speedup:
            break
        steps = traverse_next_neighbors(cur, prev)
        for step in steps:
            total_num += num_shortcuts(cur, step, grid, speedup)

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
    speedup = 74 if example else 100
    res = find_paths(grid, length, speedup)
    print(res)
    return res


assert main(True) == 10
main()
