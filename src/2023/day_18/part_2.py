import math
from collections import defaultdict
from typing import Optional

from utils.utils import *

dir_map = {
    "U": go_up,
    "D": go_down,
    "R": go_right,
    "L": go_left
}

class Corner:
    def __init__(self, r, c, direction, n):
        self.r = r
        self.c = c
        self.direction = direction
        self.n = n
        self.next: Optional[Corner] = None
        self.prev: Optional[Corner] = None

    def remove(self):
        if self.next:
            self.next.prev = self.prev
        if self.prev:
            self.prev.next = self.next

def URD(n_up, n_right, n_down):
    return max(0, n_up - n_down), n_right, max(0, n_down - n_up), min(n_up, n_down)*(n_right+1)

def RDL(n_right, n_down, n_left):
    return max(0, n_right - n_left), n_down, max(0, n_left - n_right), min(n_left, n_right) * (n_down+1)

def DLU(n_down, n_left, n_up):
    return max(0, n_down - n_up), n_left, max(0, n_up - n_down), min(n_down, n_up) * (n_left + 1)

def LUR(n_left, n_up, n_right):
    return max(0, n_left - n_right), n_up, max(0, n_right - n_left), min(n_left, n_right) * (n_up + 1)

opt_map = {
    "URD": URD,
    "RDL": RDL,
    "DLU": DLU,
    "LUR": LUR
}

opposite = {
    "U": "D",
    "D": "U",
    "L": "R",
    "R": "L"
}

def print_map(m, min_r, max_r, min_c, max_c):
    for r in range(min_r, max_r + 1):
        line = []
        for c in range(min_c, max_c + 1):
            if (r,c) == (0,0):
                line += "S"
            else:
                line += "#" if (r,c) in m else "."
        print("".join(line))

def can_opt(node1, node2, node3):
    min_r = None
    max_r = None
    min_c = None
    max_c = None
    next_node = node3.next
    if node1.n <= node3.n:
        min_r = min(node1.r, node3.r)
        max_r = max(node1.r, node3.r)
        min_c = min(node1.c, node3.c)
        max_c = max(node1.c, node3.c)
    if node1.n > node3.n:
        if next_node:
            r,c = next_node.r, next_node.c
        else:
            r, c = dir_map[node3.direction](node3.r, node3.c)
        min_r = min(node2.r, r)
        max_r = max(node2.r, r)
        min_c = min(node2.c, c)
        max_c = max(node2.c, c)

    cur_node = node3.next
    while cur_node != node1:
        if cur_node not in (node1, node2, node3, next_node):
            if min_r <= cur_node.r <= max_r and min_c <= cur_node.c <= max_c:
                return False
        assert cur_node.next
        cur_node = cur_node.next
    return True

def optimize_two_nodes(cur_node: Corner):
    next_node = cur_node.next
    if not next_node:
        return cur_node, 0, False

    if next_node.direction == cur_node.direction:
        cur_node.n += next_node.n
        next_node.remove()
        return cur_node, 0, True

    if next_node.direction == opposite[cur_node.direction]:
        if next_node.n == cur_node.n:
            chunk_size = next_node.n # not sure about this =S
            if cur_node.prev == next_node and next_node.next == cur_node:
                return None, chunk_size + 1, True
            next_node.remove()
            cur_node.remove()
            cur_node = next_node.next if next_node.next else cur_node.prev
            return cur_node, chunk_size, True
        if next_node.n < cur_node.n:
            chunk_size = next_node.n   # not sure about this =S
            cur_node.n -= next_node.n
            next_node.remove()
            return cur_node, chunk_size, True
        if next_node.n > cur_node.n:
            chunk_size = cur_node.n   # not sure about this =S
            next_node.n -= cur_node.n
            cur_node.remove()
            return next_node, chunk_size, True
    return cur_node, 0, False

def optimize_three_nodes(cur_corner: Corner):
    corner1 = cur_corner
    corner2 = corner1.next
    corner3 = corner2.next if corner2 else None
    if not corner2 or not corner3:
        return cur_corner, 0, False
    code = corner1.direction + corner2.direction + corner3.direction
    if code not in opt_map:
        return cur_corner, 0, False
    if not can_opt(corner1, corner2, corner3):
        return cur_corner, 0, False
    func = opt_map[code]
    n_1, n_2, n_3, removed_chunk = func(corner1.n, corner2.n, corner3.n)
    corner1.n = n_1
    corner2.n = n_2
    corner3.n = n_3
    if not n_3:
        corner3.remove()
    if not n_1:
        corner1.remove()
        cur_corner = corner2
    assert n_2
    return cur_corner, removed_chunk, True

def traverse_border_and_split(start_corner: Corner):
    lagoon_size = 0
    cur_corner = start_corner
    while cur_corner:
        cur_corner, removed_chunk, did_optimization = optimize_two_nodes(cur_corner)
        lagoon_size += removed_chunk
        if not did_optimization:
            cur_corner, removed_chunk, did_optimization = optimize_three_nodes(cur_corner)
            lagoon_size += removed_chunk
        if not did_optimization:
            cur_corner = cur_corner.next
    return lagoon_size

def get_from_colour(hex_c):
    hex_to_direction_map = {
        "0": "R",
        "1": "D",
        "2": "L",
        "3": "U"
    }
    direction = hex_to_direction_map[hex_c[-2]]
    number = int(hex_c[2:-2], 16)
    return direction, number


def main(example=False):
    cur = (0,0)
    prev_corner = None
    start_corner = None
    for line in read_file(example):
        direction, number, colour = line.split(" ")
        direction, number = get_from_colour(colour)
        corner = Corner(cur[0], cur[1], direction, number)
        if prev_corner:
            prev_corner.next = corner
            corner.prev = prev_corner
        if not start_corner:
            start_corner = corner
        cur = dir_map[direction](cur, n=number)
        prev_corner = corner
    assert cur == (0,0)
    start_corner.prev = prev_corner
    prev_corner.next = start_corner

    cur = start_corner
    while cur.next != start_corner:
        assert cur.prev
        assert cur.next
        cur = cur.next
    assert cur.prev
    assert cur.next

    res = traverse_border_and_split(start_corner)
    print(res)
    return res


assert main(True) == 952408144115
main()


