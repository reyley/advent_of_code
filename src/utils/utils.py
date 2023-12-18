def read_file(example=False):
    file = "example" if example else"input"
    with open(file) as f:
        for x in f:
            yield x.strip()


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

def is_up(prev, cur):
    return prev[0] < cur[0]

def is_down(prev, cur):
    return prev[0] > cur[0]

def is_left(prev, cur):
    return prev[1] > cur[1]

def is_right(prev, cur):
    return prev[1] < cur[1]

def go_up(cur):
    return cur[0] - 1, cur[1]

def go_down(cur):
    return cur[0] + 1, cur[1]

def go_left(cur):
    return cur[0], cur[1] + 1

def go_right(cur):
    return cur[0], cur[1] - 1


