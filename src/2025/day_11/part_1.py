from utils.utils import *

paths = {}

@cache
def n_paths(source):
    n = 0
    for path in paths[source]:
        if path == "out":
            n += 1
        else:
            n += n_paths(path)
    return n


def main(example=False):
    n_paths.cache_clear()
    global paths
    paths = dict()
    for line in read_file(example):
        source, ps = line.split(": ")
        ps = ps.split(" ")
        paths[source] = ps
    res = n_paths("you")
    print(res)
    return res


assert main(True) == 5
main()