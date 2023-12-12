from utils.utils import read_file

def is_up(prev, cur):
    return prev[0] < cur[0]

def is_down(prev, cur):
    return prev[0] > cur[0]

def is_left(prev, cur):
    return prev[1] > cur[1]

def is_right(prev, cur):
    return prev[1] < cur[1]

def go_up(cur):
    return cur[0] - 1, cur[1]

def go_down(cur):
    return cur[0] + 1, cur[1]

def go_left(cur):
    return cur[0], cur[1] + 1

def go_right(cur):
    return cur[0], cur[1] - 1

def find_next(prev, cur, grid):
    cur_char = grid[cur[0]][cur[1]]
    if cur_char == "|":
        if is_up(prev, cur):
            return go_down(cur)
        if is_down(prev, cur):
            return go_up(cur)
    if cur_char == "-":
        if is_left(prev, cur):
            return go_right(cur)
        if is_right(prev, cur):
            return go_left(cur)
    if cur_char == "L":
        if is_up(prev, cur):
            return go_left(cur)
        if is_left(prev, cur):
            return go_up(cur)
    if cur_char == "J":
        if is_up(prev, cur):
            return go_right(cur)
        if is_right(prev, cur):
            return go_up(cur)
    if cur_char == "7":
        if is_down(prev, cur):
            return go_right(cur)
        if is_right(prev, cur):
            return go_down(cur)
    if cur_char == "F":
        if is_down(prev, cur):
            return go_left(cur)
        if is_left(prev, cur):
            return go_down(cur)
    return None

def find_point_after_start(start, grid):

    for offset in (1, -1):
        for i in (0, 1):
            cur = list(start)
            cur[i] += offset
            try:
                res = find_next(start, cur, grid)
                if res:
                    return cur
            except Exception:
                continue


def travers(start, grid):
    prev = start
    cur = find_point_after_start(start, grid)
    circle = {tuple(start)}
    count = 1
    while grid[cur[0]][cur[1]] != "S":
        circle.add(tuple(cur))
        new_cur = find_next(prev, cur, grid)
        prev, cur = cur, new_cur
        count += 1
    return circle


def fill_empties(circle, grid):
    empties = []
    for r, row in enumerate(grid):
        for c in range(len(row)):
            if (r,c) not in circle:
                grid[r][c] = "."
                empties.append((r,c))
    return empties


def find_how_many_in_circle(empties, grid):
    in_circle = 0
    for r,c in empties:
        how_many_pipes = 0
        start_line = None
        for other_c in range(c, len(grid[0])):
            if grid[r][other_c] == "|":
                how_many_pipes += 1
            if grid[r][other_c] == "-":
                assert start_line is not None
            if grid[r][other_c] in ["F", "L"]:
                assert start_line is None
                start_line = grid[r][other_c]
            if grid[r][other_c] == "J" and start_line == "F":
                how_many_pipes += 1
                start_line = None
            if grid[r][other_c] == "J" and start_line == "L":
                start_line = None
            if grid[r][other_c] == "7" and start_line == "F":
                start_line = None
            if grid[r][other_c] == "7" and start_line == "L":
                start_line = None
                how_many_pipes += 1
        if how_many_pipes % 2 == 1:
            print(r,c)
            in_circle += 1
    return in_circle

def main(example=False):
    grid = []
    start = None
    for r, line in enumerate(read_file(example)):
        grid.append(list(line))
        for c, char in enumerate(line):
            if char == "S":
                start = r,c
    circle = travers(start, grid)
    empties = fill_empties(circle, grid)
    res = find_how_many_in_circle(empties, grid)
    print(res)
    return res


assert main(True) == 8
main()
