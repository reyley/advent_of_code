from datetime import datetime

from utils.utils import read_file

def move(func):
    def inner(self):
        self.all.remove(self)
        self.rocks_by_row[self.r].remove(self)
        self.rocks_by_column[self.c].remove(self)
        func(self)
        assert self not in self.all and self not in self.rocks_by_row[self.r] and self not in self.rocks_by_column[self.c]
        self.all.add(self)
        self.rocks_by_row[self.r].add(self)
        self.rocks_by_column[self.c].add(self)
    return inner



class Rock:
    rocks_by_row = {}
    rocks_by_column = {}
    all = set()
    cycle_states = {} # state -> cycle

    def __init__(self, r, c, char):
        self.r = r
        self.c = c
        self.is_cube = char == "#"
        self.char = char
        self.start_cycle = None
        assert char in ("#", "O")

    def weight(self):
        if self.is_cube:
            return 0
        return self.n_rows() - self.r

    def __hash__(self):
        return hash((self.r, self.c))

    def __eq__(self, other):
        return hash(other) == hash(self)

    def __repr__(self):
        return f"{self.char}({self.r}, {self.c})"

    @move
    def move_north(self):
        while (self.r - 1, self.c) not in self.all and self.r > 0:
            self.r -= 1

    @move
    def move_south(self):
        while (self.r + 1, self.c) not in self.all and self.r < self.n_rows() - 1:
            self.r += 1

    @move
    def move_west(self):
        while (self.r, self.c - 1) not in self.all and self.c > 0:
            self.c -= 1

    @move
    def move_east(self):
        while (self.r, self.c + 1) not in self.all and self.c < self.n_cols() - 1:
            self.c += 1

    @classmethod
    def n_rows(cls):
        return len(cls.rocks_by_row)

    @classmethod
    def n_cols(cls):
        return len(cls.rocks_by_column)

    @classmethod
    def cycle(cls):
        for i in range(cls.n_rows()):
            for rock in cls.rocks_by_row[i].copy():
                rock.move_north()

        for i in range(cls.n_cols()):
            for rock in cls.rocks_by_column[i].copy():
                rock.move_west()

        for i in range(cls.n_rows() - 1, -1, -1):
            for rock in cls.rocks_by_row[i].copy():
                rock.move_south()

        for i in range(cls.n_cols() - 1, -1, -1):
            for rock in cls.rocks_by_column[i].copy():
                rock.move_east()
        cls.check()

    @classmethod
    def check(cls):
        for rock in cls.all:
            if rock.is_cube:
                continue
            if rock not in cls.rocks_by_column[rock.c]:
                assert rock in cls.rocks_by_column[rock.c]
            if rock not in cls.rocks_by_row[rock.r]:
                assert rock in cls.rocks_by_row[rock.r]
    @classmethod
    def state(cls):
        return hash(frozenset((x.r, x.c) for x in cls.all if not x.is_cube))

    @classmethod
    def get_weights(cls):
        total1 = 0
        for rock in cls.all:
            total1 += rock.weight()
        total2 = 0
        for col in cls.rocks_by_column.values():
            for rock in col:
                total2 += rock.weight()
        total3 = 0
        for row in cls.rocks_by_row.values():
            for rock in row:
                total3 += rock.weight()
        assert total2 == total3
        assert total1 == total2
        assert total1 == total3
        return total3

def main(example=False):
    Rock.rocks_by_row = {}
    Rock.rocks_by_column = {}
    Rock.all = set()
    Rock.cycle_states = {} # state -> cycle

    for r, line in enumerate(read_file(example)):
        Rock.rocks_by_row[r] = set()
        for c, char in enumerate(line):
            if r == 0:
                for i in range(len(line)):
                    Rock.rocks_by_column[c] = set()
            if char != ".":
                rock = Rock(r,c,char)
                Rock.all.add(rock)
                if not rock.is_cube:
                    Rock.rocks_by_row[r].add(rock)
                    Rock.rocks_by_column[c].add(rock)

    n_cycles = 1000000000
    n_cycle = 0
    len_loop = n_cycles
    no_loop = True
    while no_loop and n_cycle < n_cycles:
        if n_cycle % 1000 == 0:
            print(datetime.now(), n_cycle)
        Rock.cycle()
        n_cycle += 1
        print(f"cycle: {n_cycle}, w: {Rock.get_weights()}")
        # print(n_cycle, Rock.get_weights())
        state = Rock.state()
        if state in Rock.cycle_states:
            no_loop = False
            len_loop = n_cycle - Rock.cycle_states[state]
            print(n_cycle, len_loop)

        else:
            Rock.cycle_states[Rock.state()] = n_cycle

    n_left = (n_cycles - n_cycle) % len_loop
    n_cycle = n_cycles - n_left
    # while n_cycle + len_loop < n_cycles:
    #     n_cycle += len_loop
    for i in range(n_left):
        Rock.cycle()
        print(f"cycle: {n_cycle + i + 1}, w: {Rock.get_weights()}")

    res = Rock.get_weights()

    print(res)
    return res


assert main(True) == 64
main()
