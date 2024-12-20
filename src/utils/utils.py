from collections import defaultdict
import re
from functools import cache
from typing import Any


class Grid:

    def __init__(self, start_ch=None):
        self.n_rows = 0
        self.n_cols = 0
        self.map = {}
        self.start = None
        self.end = None
        self.start_ch = start_ch

    def __getitem__(self, item):
        return self.map[item]

    def __setitem__(self, key, value):
        return self.add(key[0], key[1], value)

    def set_start(self, start):
        self.start = start

    def add(self, r, c, ch: Any):
        self.map[(r, c)] = ch
        self.n_rows = max(self.n_rows, r + 1)
        self.n_cols = max(self.n_cols, c + 1)
        if ch == self.start_ch:
            self.start = (r,c)

    def get(self,x, default=None):
        try:
            return self.map[x]
        except:
            return default

    def print(self, special_location=None):
        line = []
        for r in range(self.n_rows):
            for c in range(self.n_cols):
                line.append(str(self.map[(r,c)]) if (r,c) != special_location else "~")
                if c == self.n_cols - 1:
                    print("".join(line))
                    line = []


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
    file = "example" if example else "input"
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

def go_by_arrow(cur, arrow, n=1):
    if arrow == "^":
        return go_up(cur,n)
    if arrow == "v":
        return go_down(cur,n)
    if arrow == ">":
        return go_right(cur,n)
    if arrow == "<":
        return go_left(cur,n)


def clockwise(arrow, n=1):
    arrows = ["^", ">", "v", "<"]
    i = arrows.index(arrow)
    return arrows[(i + n) % len(arrows)]


def traverse_neighbors(cur):
    return [(cur[0], cur[1] + 1), (cur[0] + 1, cur[1]), (cur[0], cur[1] - 1), (cur[0] - 1, cur[1])]


@cache
def traverse_neighbors_horizontal(cur):
    res = set()
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if i != 0 or j != 0:
                res.add((cur[0] + i, cur[1] + j))
    return res

def mul(items):
    m = 1
    for x in items:
        m *= x
    return m