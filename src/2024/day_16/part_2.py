import heapq
import math

from utils.utils import *


def lowest_score(grid):
    score = 0
    cur = grid.start
    routes = [(score, cur, ">", {cur})]
    history = dict()
    best_path_score = None
    best_path_tiles = {cur}
    while routes:
        score, cur, direction, path = heapq.heappop(routes)
        if best_path_score and score > best_path_score:
            break
        if history.get((cur, direction), math.inf) < score:
            continue
        history[(cur, direction)] = score
        forward = go_by_arrow(cur, direction)
        if grid.get(forward) == "E":
            if not best_path_score:
                best_path_score = score
            if best_path_score == score:
                best_path_tiles.update(path)
                best_path_tiles.add(forward)
        elif grid.get(forward) != "#":
            heapq.heappush(routes, (score + 1, forward, direction, path.union({forward})))
        for x in [clockwise(direction, 1), clockwise(direction, 3)]:
            heapq.heappush(routes, (score + 1000, cur, x, path))
    return len(best_path_tiles)


def main(example=False):
    grid = Grid(start_ch="S")
    for r,c,ch in read_map(example):
        grid[(r,c)] = ch
    res = lowest_score(grid)
    print(res)
    return res


assert main(True) == 45
main()
