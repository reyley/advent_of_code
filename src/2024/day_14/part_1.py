from utils.utils import *

reg = re.compile("p=([-\d]+),([-\d]+) v=([-\d]+),([-\d]+)")


def move(start, v, n, n_rows, n_cols):
    print(start, v)
    end_r = (start[0] + n*v[0]) % n_rows
    end_c = (start[1] + n*v[1]) % n_cols
    print(end_r, end_c)
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


def main(example=False):
    new_locations = []
    n_cols = 11 if example else 101
    n_rows = 7 if example else 103
    for line in read_file(example):
        for c,r,vc,vr in reg.findall(line):
            start = (int(r), int(c))
            v = (int(vr), int(vc))
            new_locations.append(move(start, v, 100, n_cols=n_cols, n_rows=n_rows))
    res = count_quadrants(new_locations, n_cols, n_rows)
    print(res)
    return res


assert main(True) == 12
main()
