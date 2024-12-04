from utils.utils import *
from itertools import combinations

directions = [
    (1,1),
    (1,-1),
    (-1,-1),
    (-1,1)
]


def get(xmas_map, row, col):
    if row < 0 or col < 0:
        return "#"
    try:
        return xmas_map[row][col]
    except Exception:
        return "#"


def count_x_mas_in_location(row_i, col_j, xmas_map):
    count = 0
    mas_list = [get(xmas_map, row_i + i, col_j + j) for i , j in directions]
    mas_str = "".join([get(xmas_map, row_i + i, col_j + j) for i , j in directions])
    mas_list.sort()
    if ("MM" in mas_str or "SS" in mas_str) and mas_list == ["M", "M", "S", "S"]:
        count += 1
    return count


def count_xmas(xmas_map):
    res = 0
    for row_i, row in enumerate(xmas_map):
        for col_j, char in enumerate(row):
            if char == "A":
                res += count_x_mas_in_location(row_i, col_j, xmas_map)
    return res


def main(example=False):
    xmas_map = []
    for line in read_file(example):
        xmas_map.append(line)
    res = count_xmas(xmas_map)
    print(res)
    return res


assert main(True) == 9
main()
