from pprint import pprint

from utils.utils import read_file

def distance(gal_1, gal_2):
    return abs(gal_1[0] - gal_2[0]) + abs(gal_1[1] - gal_2[1])

def count_distances(galaxies):
    dists = 0
    for i, gal_1 in enumerate(galaxies):
        for gal_2 in galaxies[i+1:]:
            dists += distance(gal_1, gal_2)
    return dists

def adjust(galaxies, by_list, idx):
    galaxies.sort(key= lambda x:x[idx])
    g_idx = 0
    b_idx = 0
    while g_idx < len(galaxies):
        if b_idx >= len(by_list):
            galaxies[g_idx][idx] += len(by_list) * 999999
            g_idx += 1
        elif by_list[b_idx] > galaxies[g_idx][idx]:
            galaxies[g_idx][idx] += b_idx * 999999
            g_idx += 1
        elif by_list[b_idx] < galaxies[g_idx][idx]:
            b_idx += 1
        else:
            assert by_list[b_idx] != galaxies[g_idx][idx]

def main(example=False):
    galaxies = []
    rows = set()
    columns = set()
    for r, line in enumerate(read_file(example)):
        rows.add(r)
        for c, char in enumerate(line):
            if r == 0 and c == 0:
                columns.update(set(range(len(line))))
            if char == "#":
                galaxies.append([r,c])
                rows.discard(r)
                columns.discard(c)
    rows = sorted(rows)
    columns = sorted(columns)
    adjust(galaxies, rows, 0)
    adjust(galaxies, columns, 1)
    res = count_distances(galaxies)
    print(res)
    return res


# assert main(True) == 1030
main()
