import heapq

from utils.utils import *


def lowest_score(grid):
    score = 1
    cur = grid.start
    routes = [(score, cur, (cur,))]
    history = set()
    while routes:
        score, cur, cur_route = heapq.heappop(routes)
        if cur in history:
            continue
        history.add(cur)
        nexts = traverse_neighbors(cur)
        for spot in nexts:
            if spot == grid.end:
                return score
            elif grid.get(spot) == ".":
                heapq.heappush(routes, (score + 1, spot, cur_route + (spot,)))
    return None


def main(example=False):
    n = 12 if example else 1024
    grid_n = 7 if example else 71
    grid = Grid()
    grid.end = (grid_n - 1, grid_n - 1)
    grid.start = (0,0)
    for i, line in enumerate(read_file(example)):
        if i == n:
            break
        c,r = int_line(line)
        grid[(r,c)] = "#"
    for r in range(grid_n):
        for c in range(grid_n):
            if grid.get((r,c)) != "#":
                grid.add(r,c,".")
    res = lowest_score(grid)
    print(res)
    return res


assert main(True) == 22
main()
