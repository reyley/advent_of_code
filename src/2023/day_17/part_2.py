from utils.utils import *
from heapq import *

class Path:
    map = {}
    max_same_direction = 10
    min_same_direction = 3
    end = None
    def __init__(self, prev, cur, heat=0, n_same_directions=1):
        self.prev = prev
        self.cur = cur
        self.heat = heat
        self.n_same_directions = n_same_directions

    def key(self):
        return self.cur, self.prev, self.n_same_directions

    def __lt__(self, other):
        return self.heat.__lt__(other.heat)

    def next(self):
        go_same_direction = None
        go_other_directions = None
        if is_up(self.prev, self.cur):
            go_same_direction = go_down
            go_other_directions = go_right, go_left
        elif is_down(self.prev, self.cur):
            go_same_direction = go_up
            go_other_directions = go_right, go_left
        elif is_left(self.prev, self.cur):
            go_same_direction = go_left
            go_other_directions = go_up, go_down
        elif is_right(self.prev, self.cur):
            go_same_direction = go_right
            go_other_directions = go_up, go_down

        outputs = []
        if go_other_directions and self.n_same_directions < self.max_same_direction :
            _next = go_same_direction(self.cur)
            if _next in self.map:
                heat = self.map[_next]
                outputs.append(Path(self.cur, _next, self.heat + heat, self.n_same_directions + 1))
        if go_other_directions and self.n_same_directions > self.min_same_direction:
            for go_direction in go_other_directions:
                _next = go_direction(self.cur)
                if _next in self.map:
                    heat = self.map[_next]
                    outputs.append(Path(self.cur, _next, self.heat + heat))
        return outputs

    def is_end(self):
        return self.cur == self.end

def traverse():
    start1 = Path(prev=(-1,0), cur=(0,0), n_same_directions=0)
    start2 = Path(prev=(0, -1), cur=(0, 0), n_same_directions=0)
    heap = [(0, start1), (0, start2)]
    history = set()

    while heap:
        path_size, path = heappop(heap)
        if path.key() in history:
            continue
        history.add(path.key())
        if path.is_end() and path.n_same_directions > path.min_same_direction:
            return path_size
        next_paths = path.next()
        for p in next_paths:
            if p.key() not in history:
                print(p.heat, p.cur)
                heappush(heap, (p.heat, p))
    assert False


def main(example=False):
    Path.end = (0,0)
    for r,c,char in read_map(example):
        Path.map[(r,c)] = int(char)
        if (r,c) > Path.end:
            Path.end = (r,c)

    res = traverse_neighbors()
    print(res)
    return res


assert main(True) == 94
main()
