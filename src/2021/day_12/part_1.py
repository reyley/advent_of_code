from utils.utils import read_file

def count(nodes):
    unique_paths = set()
    paths = [["start", n] for n in nodes["start"]]
    while len(paths) > 0:
        path = paths.pop()
        if path[-1] == "end":
            unique_paths.add(tuple(path))
            continue
        else:
            new_paths = []
            for k in nodes[path[-1]]:
                if k == k.lower() and k in path:
                    continue
                new_path = path + [k]
                loop = False
                # for i in range(2, len(new_path)//2):
                #     if new_path[-(i*2):-i] == new_path[-i:]:
                #         loop = True
                if not loop:
                    new_paths.append(new_path)
            paths.extend(new_paths)
    return len(unique_paths)


def add(var1, var2, paths):
    if var2 != "start" and var1 != "end":
        if var1 not in paths:
            paths[var1] = {var2}
        else:
            paths[var1].add_line(var2)

def main(example=False):
    paths = {}
    for line in read_file(example):
        a, b = line.split("-")
        add(a, b, paths)
        add(b, a, paths)

    res = count(paths)
    print(res)
    return res


assert main(True) == 226
main()
