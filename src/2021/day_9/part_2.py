from utils.utils import read_file


def is_low_point(i,j,lines):
    h = lines[i][j]
    for n_i, n_j in [(i,j + 1), (i, j -1), (i + 1, j), (i - 1, j)]:
        if n_i >= 0 and n_j >= 0:
            try:
                option = lines[n_i][n_j]
                if option <= h:
                    return False
            except:
                pass
    print(h)
    return True

def get_basin_size(i, j, lines):
    basin = set([(i, j)])
    lines_to_try = [(i, j)]
    while len(lines_to_try) > 0:
        i, j = lines_to_try.pop()
        for n_i, n_j in [(i,j + 1), (i, j -1), (i + 1, j), (i - 1, j)]:
            if n_i >= 0 and n_j >= 0:
                try:
                    if (n_i, n_j) not in basin and lines[n_i][n_j] != "9":
                        basin.add((n_i, n_j))
                        lines_to_try.append((n_i, n_j))
                except:
                    pass
    return len(basin)


def main(example=False):
    lines = list(read_file(example))
    basin_sizes = []
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if is_low_point(i,j,lines):
                basin_sizes.append(get_basin_size(i,j,lines))
    res = 1
    basin_sizes.sort(reverse=True)
    max_basins = basin_sizes[:3]
    for x in max_basins:
        res *= x
    print(res)
    return res


assert main(True) == 1134
main()
