from utils.utils import read_file


def drop_sand(grid):
    cur = (0, 500)
    is_ok = True
    while is_ok:
        try:
            n = cur[0]+1, cur[1]
            val = grid[n[0]][n[1]]
            if val == ".":
                cur = n
                continue
            if val in ["#", "0"]:
                n = cur[0] + 1, cur[1] - 1
                val = grid[n[0]][n[1]]
                if val == ".":
                    cur = n
                    continue
                n = cur[0] + 1, cur[1] + 1
                val = grid[n[0]][n[1]]
                if val == ".":
                    cur = n
                    continue
                else:
                    break
        except:
            assert False
            is_ok = False
            continue
    if is_ok:
        grid[cur[0]][cur[1]] = "0"
    if cur == (0, 500):
        is_ok = False
    return is_ok


def print_grid(grid):
    for _ in grid:
        print(_)


def count_sand(grid):
    res = 0
    while drop_sand(grid):
        # print_grid(grid)
        res += 1
    return res


def fill(grid, lines):
    for line in lines:
        for k in range(len(line) - 1):
            i1, j1 = line[k]
            i2, j2 = line[k+1]
            if i1 == i2:
                max_j = max(j1, j2)
                min_j = min(j1, j2)
                for j in range(min_j, max_j+1):
                    grid[i1][j] = "#"
            if j1 == j2:
                max_i = max(i1, i2)
                min_i = min(i1, i2)
                for i in range(min_i, max_i+1):
                    grid[i][j1] = "#"
    grid.append(["."])


def main(example=False):
    lines = []
    max_i = 0
    max_j = 0
    for line in read_file(example):
        points = line.split(" -> ")
        lines.append([])
        for point in points:
            x,y = point.split(",")
            lines[-1].append((int(y), int(x)))
            if int(x) > max_i:
                max_i = int(x)
            if int(y) > max_j:
                max_j = int(y)
    grid = [["."]*(max_i+max_j+1) for _ in range(max_j + 2)]
    grid.append(["#"]*(max_i+max_j+1))
    fill(grid, lines)
    print_grid(grid)
    res = count_sand(grid)
    print_grid(grid)
    print(res)
    return res + 1


assert main(True) == 93
print(main())
