from utils.utils import read_file

def count(nodes):
    unique_paths = set()
    paths = [(["start", n], False) for n in nodes["start"]]
    while len(paths) > 0:
        path, has_double = paths.pop()
        if path[-1] == "end":
            unique_paths.add(tuple(path))
            continue
        else:
            new_paths = []
            for k in nodes[path[-1]]:
                has_double_in_this_path = has_double
                if k == k.lower():
                    if has_double and k in path:
                        continue
                    if not has_double:
                        c = path.count(k)
                        if c > 1:
                            continue
                        has_double_in_this_path = False if c == 0 else True
                new_path = path + [k]
                new_paths.append((new_path, has_double_in_this_path))
            paths.extend(new_paths)
    for i in sorted(list(unique_paths)):
        print(i)
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


assert main(True) == 36
main()
