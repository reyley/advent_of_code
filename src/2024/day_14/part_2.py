from utils.utils import *

reg = re.compile("p=([-\d]+),([-\d]+) v=([-\d]+),([-\d]+)")


def move(start, v, n, n_rows, n_cols):
    # print(start, v)
    end_r = (start[0] + n*v[0]) % n_rows
    end_c = (start[1] + n*v[1]) % n_cols
    # print(end_r, end_c)
    return end_r, end_c


def count_quadrants(new_locations, n_cols, n_rows):
    qds = [0]*4
    mid_cols = n_cols//2
    mid_rows = n_rows//2
    for x,y in new_locations:
        if x < mid_rows:
            if y < mid_cols:
                qds[0] += 1
            elif y > mid_cols:
                qds[1] += 1
        elif x > mid_rows:
            if y < mid_cols:
                qds[2] += 1
            elif y > mid_cols:
                qds[3] += 1
    return mul(qds)


def print_map(locations, n_cols, n_rows):
    line = []
    for r in range(n_rows):
        for c in range(n_cols):
            line.append("#" if (r,c) in locations else ".")
            if c == n_cols - 1:
                print("".join(line))
                line = []


def is_symmetrical(locations, n_cols):
    for loc in locations:
        if (loc[0], n_cols-loc[1]-1) not in locations:
            return False
    return True


def most_neighbors(locations):
    n_neighbors = 0
    for loc in locations:
        neighbors = traverse_neighbors_horizontal(loc)
        x = neighbors.intersection(locations)
        if not x:
            continue
        n_neighbors += 1
    return n_neighbors >= len(locations)//1.5


def main(example=False):
    start_v = []
    n_cols = 11 if example else 101
    n_rows = 7 if example else 103
    for line in read_file(example):
        for c,r,vc,vr in reg.findall(line):
            start = (int(r), int(c))
            v = (int(vr), int(vc))
            start_v.append((start,v))
    for i in range(10403):  # loop number
        new_locations = set()
        new_locations_v = []
        for start, v in start_v:
            new_loc = move(start, v, i, n_cols=n_cols, n_rows=n_rows)
            new_locations.add(new_loc)
            new_locations_v.append((new_loc,v))
        if new_locations_v == start_v and i > 0:
            break
        if most_neighbors(new_locations):
            print("$" * 200)
            print(i)
            print_map(new_locations, n_cols, n_rows)
        # well this wasn't useful
        # if is_symmetrical(new_locations, n_cols):
        #     print("$" * 200)
        #     print(i)
        #     print_map(new_locations, n_cols, n_rows)
    res = 0
    print(res)
    return res


# assert main(True) == 12
main()
