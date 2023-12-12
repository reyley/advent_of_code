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
    count = 1
    while grid[cur[0]][cur[1]] != "S":
        new_cur = find_next(prev, cur, grid)
        prev, cur = cur, new_cur
        count += 1
    return count



def main(example=False):
    grid = []
    start = None
    for r, line in enumerate(read_file(example)):
        grid.append(list(line))
        for c, char in enumerate(line):
            if char == "S":
                start = r,c
    count = travers(start, grid)
    res = count / 2
    print(res)
    return res


assert main(True) == 8
main()
