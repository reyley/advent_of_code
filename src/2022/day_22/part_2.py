from utils.utils import read_file_not_strip

faces = {
    1: [0, 100],
    2: [0, 50],
    3: [50, 50],
    4: [100, 50],
    5: [100, 0],
    6: [150, 0]
}

faces_example = {

}

face_size = 50


def face(row,col):
    for f in faces:
        if faces[f][0] <= row < faces[f][0] + face_size and \
                faces[f][1] <= col < faces[f][1] + face_size:
            print(f)
            return f
    assert False


def convert(row, col, ori):
    print(f"old: r:{row}, c:{col}, or:{ori}")
    f = face(row, col)
    if f == 1 and ori == 0:
        new_ori = 2
        new_col = 99
        new_row = 149 - row
    elif f == 1 and ori == 1:
        new_ori = 2
        new_row = col - 50
        new_col = 99
    elif f == 1 and ori == 3:
        new_ori = 3
        new_col = col - 100
        new_row = 199
    elif f == 2 and ori == 3:
        new_ori = 0
        new_row = 100 + col
        new_col = 0
    elif f == 2 and ori == 2:
        new_ori = 0
        new_row = 149 - row
        new_col = 0
    elif f == 3 and ori == 0:
        new_ori = 3
        new_row = 49
        new_col = 50 + row
    elif f == 3 and ori == 2:
        new_ori = 1
        new_row = 100
        new_col = row - 50
    elif f == 4 and ori == 0:
        new_ori = 2
        new_row = 149 - row
        new_col = 149
    elif f == 4 and ori == 1:
        new_ori = 2
        new_row = 100 + col
        new_col = 49
    elif f == 5 and ori == 2:
        new_ori = 0
        new_row = 149 - row
        new_col = 50
    elif f == 5 and ori == 3:
        new_ori = 0
        new_row = 50 + col
        new_col = 50
    elif f == 6 and ori == 0:
        new_ori = 3
        new_row = 149
        new_col = row - 100
    elif f == 6 and ori == 1:
        new_ori = 1
        new_col = 100 + col
        new_row = 0
    elif f == 6 and ori == 2:
        new_ori = 1
        new_col = row - 100
        new_row = 0
    else:
        assert False
    print(f"new: r:{new_row}, c:{new_col}, or:{new_ori}")
    return new_row, new_col, new_ori


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
            return
        elif inp == "L":
            self.orientation = (self.orientation - 1 ) % 4
            return

        for i in range(inp):
            if self.orientation in [0, 2]:
                dir = 1 if self.orientation == 0 else -1
                new_col = self.get_col(self.col + dir)
                if new_col != self.col + dir:
                    new_row, new_col, new_orientation = convert(self.row, self.col, self.orientation)
                else:
                    new_row, new_orientation = self.row, self.orientation
                chr = self.map.get(new_row, new_col)
                assert chr in ["#", "."]
                if chr == "#":
                    break
                else:
                    assert self.col != new_col
                    self.col = new_col
                    self.row = new_row
                    self.orientation = new_orientation
                    a = self.map.chrs[new_orientation]
                m[self.row][self.col] = a
            elif self.orientation in [1, 3]:
                dir = 1 if self.orientation == 1 else -1
                new_row = self.get_row(self.row + dir)
                if new_row != self.row + dir:
                    new_row, new_col, new_orientation = convert(self.row, self.col, self.orientation)
                else:
                    new_col, new_orientation = self.col, self.orientation
                chr = self.map.get(new_row, new_col)
                assert chr in ["#", "."]
                if chr == "#":
                    break
                else:
                    assert self.row != new_row
                    self.col = new_col
                    self.row = new_row
                    self.orientation = new_orientation
                    a = self.map.chrs[new_orientation]
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
