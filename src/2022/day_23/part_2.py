from typing import List

from utils.utils import read_file


class Elf:

    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.next = None

    def __str__(self):
        return "#"

    def __repr__(self):
        return f"{self.r=} {self.c=}"

    def next_move(self, m, r):
        self.next = self.calc_next_move(m, r)
        # print(f"r:{self.r}, c:{self.c} Next: {self.next}")
        return self.next

    def calc_next_move(self, m, round):
        should_move = False
        for i in [0, 1, -1]:
            for j in [0, 1, -1]:
                if i == j == 0:
                    continue
                if m[self.r + i][self.c + j] != ".":
                    should_move = True
                    break
        if not should_move:
            return None
        for k in range(round, round + 4):
            i = k % 4
            if i == 1 and m[self.r + 1][self.c] == m[self.r + 1][self.c + 1] == m[self.r + 1][self.c - 1] == ".":
                return self.r + 1, self.c
            if i == 0 and m[self.r - 1][self.c] == m[self.r - 1][self.c + 1] == m[self.r - 1][self.c - 1] == ".":
                return self.r - 1, self.c
            if i == 3 and m[self.r][self.c + 1] == m[self.r + 1][self.c + 1] == m[self.r - 1][self.c + 1] == ".":
                return self.r, self.c + 1
            if i == 2 and m[self.r][self.c - 1] == m[self.r + 1][self.c - 1] == m[self.r - 1][self.c - 1] == ".":
                return self.r, self.c - 1

    def move(self, m):
        assert self.next is not None
        m[self.r][self.c] = "."
        self.r, self.c = self.next
        m[self.r][self.c] = self
        self.next = None


class Map:
    def __init__(self, n, size):
        self.map = [["."] * (size + 2 * n) for _ in range(n)]
        self.n = n
        self.size = size
        self.elves: List[Elf] = []

    def add(self, line):
        new_line = []
        for i, ch in enumerate(line):
            if ch == "#":
                elf = Elf(len(self.map), self.n + i)
                new_line.append(elf)
                self.elves.append(elf)
            else:
                new_line.append(".")
        self.map.append(["."] * self.n + list(line) + ["."] * self.n)

    def finish(self):
        self.map.extend(["."] * (self.size + 2 * self.n) for _ in range(self.n))

    def print(self):
        for line in self.map:
            print("".join(map(str, line)))
        print("")

    def move(self, r):
        moves_e = {}
        moves_set = set()
        for e in self.elves:
            n = e.next_move(self.map, r)
            if n is None:
                continue
            if n in moves_set and n in moves_e:
                moves_e.pop(n)
            else:
                moves_set.add(n)
                moves_e[n] = e
        for e in moves_e.values():
            e.move(self.map)
        return len(moves_e)


def move(n, m):
    for r in range(n):
        n_moved = m.move(r)
        # m.print()
        if n_moved == 0:
            return r + 1


def calc_res(m):
    r = None
    c = None
    for e in m.elves:
        if r is None:
            r = [e.r, e.r]
            c = [e.c, e.c]
        else:
            r[0] = min(r[0], e.r)
            r[1] = max(r[1], e.r)
            c[0] = min(c[0], e.c)
            c[1] = max(c[1], e.c)
    print(r, c)
    return (r[1] - r[0] + 1) * (c[1] - c[0] + 1) - len(m.elves)


def main(example=False):
    m = None
    n = 1000
    for line in read_file(example):
        if m is None:
            m = Map(n, len(line))
        m.add(line)
    m.finish()
    # m.print()

    res = move(n, m)
    # res = calc_res(m)
    print(res)
    return res


assert main(True) == 20
print(main())
