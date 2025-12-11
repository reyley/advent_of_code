from utils.utils import *

paths = {}
counter = 0

@cache
def n_paths(source, visited_dac=False, visited_fft=False):
    n = 0
    any_visited_dac = visited_dac
    any_visited_fft = visited_fft
    for path in paths[source]:
        n_d = 0
        _visited_dac = False
        _visited_fft = False
        if path == "out" and visited_dac and visited_fft:
            n_d = 1
        elif path == "dac":
            n_d ,_visited_dac, _visited_fft = n_paths(path, True, visited_fft)
        elif path == "fft":
            n_d ,_visited_dac, _visited_fft = n_paths(path, visited_dac, True)
        elif path != "out":
            n_d ,_visited_dac, _visited_fft = n_paths(path, visited_dac, visited_fft)
        n += n_d
        if _visited_dac:
            any_visited_dac = True
        if _visited_fft:
            any_visited_fft = True
    return n ,visited_dac or any_visited_dac, visited_fft or any_visited_fft


def main(example=False):
    n_paths.cache_clear()
    global paths
    paths = dict()
    for line in read_file(example):
        source, ps = line.split(": ")
        ps = ps.split(" ")
        paths[source] = ps
    res, _, _ = n_paths("svr")
    print(res)
    return res


assert main(True) == 2
main()