from copy import deepcopy

from utils.utils import read_file


class Stream:
    def __init__(self, stream):
        self.stream = stream
        self.idx = 0

    def get(self):
        r = self.stream[self.idx]
        self.idx = (self.idx + 1) % len(self.stream)
        if r == '<':
            return [0, -1]
        return [0, 1]


def shape_line(line, w):
    return list(line) + ["."]*(w - len(line))


def make_shapes(width):
    return {
        0: [
            shape_line("..@@@@", width)
        ],
        1: [
            shape_line("...@.", width),
            shape_line("..@@@", width),
            shape_line("...@.", width)
        ],
        2: [
            shape_line("..@@@", width),
            shape_line("....@", width),
            shape_line("....@", width)
        ],
        3: [
            shape_line("..@", width),
            shape_line("..@", width),
            shape_line("..@", width),
            shape_line("..@", width)
        ],
        4: [
            shape_line("..@@", width),
            shape_line("..@@", width)
        ]
    }


def shape_loc(t, loc):
    r, c = loc
    if t == 0:
        return [
            loc,
            [r, c + 1],
            [r, c + 2],
            [r, c + 3],
        ]
    if t == 1:
        return [
            [r, c + 1],
            [r - 1, c],
            [r - 1, c + 1],
            [r - 1, c + 2],
            [r - 2, c + 1],
        ]
    if t == 2:
        return [
            [r, c + 2],
            [r - 1, c + 2],
            [r - 2, c],
            [r - 2, c + 1],
            [r - 2, c + 2],
        ]
    if t == 3:
        return [
            [r, c],
            [r - 1, c],
            [r - 2, c],
            [r - 3, c],
        ]
    if t == 4:
        return [
            [r, c],
            [r, c + 1],
            [r - 1, c],
            [r - 1, c + 1],
        ]


def get_height(tower):
    height = len(tower)
    while height > 1 and "@" not in tower[height - 1]:
        height -= 1
    return height


def add_shape(t, tower, width, shapes):
    height = get_height(tower)
    while len(tower) <= height + 3:
        tower.append(["."]*width)
    while len(tower) > height + 3:
        tower.pop(-1)
    tower.extend(deepcopy(shapes[t]))


def move_shape_stream(t, tower, stream, loc):
    locs = shape_loc(t, loc)
    direction = stream.get()
    if try_move(locs, direction, tower):
        move(locs, direction, tower)
        return [loc[0], loc[1] + direction[1]]
    return loc


def try_move(locs, direction, tower):
    for loc in locs:
        new_loc = [loc[0] + direction[0], loc[1] + direction[1]]
        if new_loc in locs:
            continue
        if new_loc[1] < 0:
            return False
        try:
            x = tower[new_loc[0]][new_loc[1]]
            if x == "@":
                return False
        except IndexError:
            return False
    return True


def move(locs, direction, tower):
    for loc in locs:
        tower[loc[0]][loc[1]] = "."
    for loc in locs:
        new_loc = loc[0] + direction[0], loc[1] + direction[1]
        tower[new_loc[0]][new_loc[1]] = "@"


def move_shape_down(t, tower, loc):
    locs = shape_loc(t, loc)
    if try_move(locs, [-1, 0], tower):
        move(locs, [-1, 0], tower)
        return [loc[0] - 1, loc[1]], False
    else:
        return loc, True


def move_shape_to_bottom(t, tower, stream):
    stopped = False
    loc = [-1, 2]
    while not stopped:
        loc = move_shape_stream(t, tower, stream, loc)
        loc, stopped = move_shape_down(t, tower, loc)


def get_tower_hight_after_rocks(n_rocks, width, s):
    stream = Stream(s)
    shapes = make_shapes(width)
    tower = []
    height = 0
    for i in range(n_rocks):
        # if i % 10 == 0:
        #     print(i, height + get_height(tower))
        #     if len(tower) > 20:
        #         height += len(tower) - 20
        #         tower = tower[-20:]
        t = i % len(shapes)
        add_shape(i % len(shapes), tower, width, shapes)
        move_shape_to_bottom(t, tower, stream)
    return height + get_height(tower)


def print_tower(tower):
    for x in tower[::-1]:
        print("".join(x))
    print("~~~~~~~~~~~~~")


def main(example=False):
    s = ""
    for line in read_file(example):
        s = line

    res = get_tower_hight_after_rocks(2022, 7, s)
    # print(res)
    # return res
    # for x in range(5, 1001, 5):
    #     res = get_tower_hight_after_rocks(x, 7, Stream(s))
    #     print(x, res)
    print(res)
    return res


# assert main(True) == 3068
print(main())
