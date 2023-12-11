import math

from utils.utils import read_file


def parse_line(line):
    d, n = line.split(" ")
    n = int(n)
    if d == "R":
        return 0, 1, n
    if d == "L":
        return 0, -1, n
    if d == "U":
        return 1, 0, n
    if d == "D":
        return -1, 0, n


def move_tail(head_location, tail_location):
    tail_location = list(tail_location)
    should_move = False
    for x in [0, 1]:
        if abs(head_location[x] - tail_location[x]) > 1:
            should_move = True
    if should_move:
        for x in [0, 1]:
            if abs(head_location[x] - tail_location[x]) == 1:
                tail_location[x] = head_location[x]
            if abs(head_location[x] - tail_location[x]) == 2:
                tail_location[x] = tail_location[x] + (head_location[x] - tail_location[x])//2
            if abs(head_location[x] - tail_location[x]) > 2:
                print(head_location, tail_location)
    return tuple(tail_location)


def move_head(head_location, i, j):
    return head_location[0] + i, head_location[1] + j


def print_grid(s):
    x = [["."]*30 for _ in range(12)]
    for i, j in s:
        x[i][j] = "#"
    for i in x:
        print(i)
    print("~"*8)


def main(example=False):
    res = 0
    visited_locations = set()
    head_location = (0, 0)
    middle = [(0, 0) for x in range(8)]
    tail_location = (0, 0)
    for line in read_file(example):
        i, j, n = parse_line(line)
        for _ in range(n):
            head_location = move_head(head_location, i, j)
            prev = head_location
            for k in range(len(middle)):
                if k > 0:
                    prev = middle[k - 1]
                middle[k] = move_tail(prev, middle[k])
            tail_location = move_tail(middle[-1], tail_location)
            visited_locations.add(tail_location)
        # print_grid(visited_locations)
        pass
    # print_grid(visited_locations)
    res = len(visited_locations)
    return res


assert main(True) == 36
print(main())
