from utils.utils import read_file_not_strip


class Directions:
    def __init__(self, line):
        self.directions = []
        n = ""
        for i in line:
            if i in ["R", "L"]:
                self.directions.append(int(n))
                n = ""
                self.directions.append(i)
            else:
                n += i
        if n:
            self.directions.append(int(n))


class Location:
    def __init__(self, _map):
        self.row = 0
        self.map: Map = _map
        self.col = self.map.row(0).start
        self.orientation = 0
        self.print(0)

    def print(self, d):
        print(f"step:{d}. row:{self.row}, col:{self.col}, d:{self.orientation}")

    def move(self, inp, m, a):
        if inp == "R":
            self.orientation = (self.orientation + 1 ) % 4
        elif inp == "L":
            self.orientation = (self.orientation - 1 ) % 4
        elif self.orientation in [0, 2]:
            dir = 1 if self.orientation == 0 else -1
            for i in range(inp):
                new_col = self.get_col(self.col + dir)
                chr = self.map.get(self.row, new_col)
                assert chr in ["#", "."]
                if chr == "#":
                    break
                else:
                    assert self.col != new_col
                    self.col = new_col
                m[self.row][self.col] = a
        elif self.orientation in [1, 3]:
            dir = 1 if self.orientation == 1 else -1
            for i in range(inp):
                new_row = self.get_row(self.row + dir)
                chr = self.map.get(new_row, self.col)
                assert chr in ["#", "."]
                if chr == "#":
                    break
                else:
                    assert self.row != new_row
                    self.row = new_row
                m[self.row][self.col] = a

    def get_row(self, n):
        dir = -1 if self.row > n else 1
        if n == len(self.map.map):
            n = 0
        if n == -1:
            n = len(self.map.map) - 1
        chr = self.map.get(n, self.col, allow=True)
        while chr == " ":
            n += dir
            if n == len(self.map.map):
                n = 0
            if n == -1:
                n = len(self.map.map) - 1
            chr = self.map.get(n, self.col, allow=True)
        return n

    def get_col(self, n):
        row = self.map.row(self.row)
        ln = len(row.line)
        assert row.start - 1 <= n <= ln
        if n == ln:
            n = row.start
        if n == row.start - 1:
            n = ln - 1
        return n

class Line:
    def __init__(self, line):
        self.start = line.count(" ")
        self.line = line


class Map:
    def __init__(self):
        self.map = []
        self.location: Location = None
        self.draw_map = []
        self.chrs = {
            0: ">",
            1: "v",
            2: "<",
            3: "^"
        }

    def add(self, line):
        self.map.append(Line(line))

    def row(self, i):
        return self.map[i]

    def setup(self):
        self.location = Location(self)
        for x in self.map:
            self.draw_map.append(list(x.line))
        self.print()

    def move(self, chr):
        arrow = self.chrs[self.location.orientation]
        self.location.move(chr, self.draw_map, arrow)
        arrow = self.chrs[self.location.orientation]
        self.draw_map[self.location.row][self.location.col] = arrow
        self.location.print(chr)

    def print(self):
        for x in self.draw_map:
            print("".join(x))

    def get(self, row, col, allow=False):
        r = self.row(row)
        try:
            return r.line[col]
        except IndexError:
            if not allow:
                assert False
            return " "


def main(example=False):
    directions = None
    _map = Map()
    parse_directions = False
    for line in read_file_not_strip(example):
        if not line.strip():
            parse_directions = True
            _map.setup()
            continue
        if parse_directions:
            directions = Directions(line)
        else:
            _map.add(line)

    # _map.location.row = 11
    # _map.location.col = 92
    # _map.location.orientation = 1
    _map.draw_map[_map.location.row][_map.location.col] = "X"
    for d in directions.directions:
        _map.move(d)
    _map.print()
    l = _map.location
    col_start = _map.row(l.row).start
    res = (l.row + 1) * 1000 + (l.col + 1) * 4 + l.orientation

    print(res)
    return res


# assert main(True) == 6032
print(main())
