from utils.utils import *

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
    mas1 = {get(xmas_map, row_i + i, col_j + j) for i , j in [(-1,-1), (1,1)]}
    mas2 = {get(xmas_map, row_i + i, col_j + j) for i, j in [(1, -1), (-1, 1)]}
    if mas1 == mas2 == {"M", "S"}:
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
