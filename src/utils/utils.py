def read_file(example=False):
    file = "example" if example else"input"
    with open(file) as f:
        for x in f:
            yield x.strip()


def read_split_file(example=False):
    part = 1
    for x in read_file(example):
        if not x:
            part += 1
        else:
            yield x.strip(), part


def read_file_not_strip(example=False):
    file = "example" if example else"input"
    with open(file) as f:
        for x in f:
            yield x.strip("\n")

def read_map(example=False):
    for r, line in enumerate(read_file(example)):
        for c, char in enumerate(line):
            yield r,c,char

def int_line(line, delim=","):
    return [int(x) for x in line.split(delim)]

def int_space_line(line, delim=", "):
    return [int(x) for x in line.split(delim)]

def is_up(prev, cur):
    return prev[0] < cur[0]

def is_down(prev, cur):
    return prev[0] > cur[0]

def is_left(prev, cur):
    return prev[1] > cur[1]

def is_right(prev, cur):
    return prev[1] < cur[1]

def go_up(cur, n=1):
    return cur[0] - n, cur[1]

def go_down(cur, n=1):
    return cur[0] + n, cur[1]

def go_right(cur, n=1):
    return cur[0], cur[1] + n

def go_left(cur, n=1):
    return cur[0], cur[1] - n

def traverse_neighbors(cur):
    return [(cur[0], cur[1] + 1), (cur[0], cur[1] - 1), (cur[0] + 1, cur[1]), (cur[0] - 1, cur[1])]

