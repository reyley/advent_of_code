import heapq

from utils.utils import *


def lowest_score(grid):
    score = 0
    cur = grid.start
    routes = [(score, cur, ">")]
    history = set()
    while routes:
        score, cur, direction = heapq.heappop(routes)
        if (cur, direction) in history:
            continue
        history.add((cur, direction))
        forward = go_by_arrow(cur, direction)
        if grid.get(forward) == "E":
            return score + 1
        elif grid.get(forward) != "#":
            heapq.heappush(routes, (score + 1, forward, direction))
        for x in [clockwise(direction, 1), clockwise(direction, 3)]:
            heapq.heappush(routes, (score + 1000, cur, x))
    return None


def main(example=False):
    grid = Grid(start_ch="S")
    for r,c,ch in read_map(example):
        grid[(r,c)] = ch
    res = lowest_score(grid)
    print(res)
    return res


assert main(True) == 7036
main()
