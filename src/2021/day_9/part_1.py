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

def main(example=False):
    lines = list(read_file(example))
    res = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            h = lines[i][j]
            if is_low_point(i,j,lines):
                res += int(h) + 1
    print(res)
    return res


assert main(True) == 15
main()
