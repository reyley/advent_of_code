from utils.utils import read_file

S = " __size__ "


def get_current_dir(dirname, current_dir):
    if dirname == "..":
        return current_dir[:-1]
    if dirname == "/":
        return []
    return current_dir + [dirname]


def add_to_sum(line, current_dir, file_system):
    size = int(line.split(" ")[0])
    file_system[S] += size
    d = file_system
    for key in current_dir:
        if key not in d:
            d[key] = {S: size}
        else:
            d[key][S] += size
        d = d[key]


def sum_dirs_le(n, file_system, total_so_far=0):
    for key in file_system:
        if key == S:
            if file_system[S] <= n:
                total_so_far += file_system[S]
        else:
            total_so_far += sum_dirs_le(n, file_system[key])
    return total_so_far



def main(example=False):
    res = 0
    current_dir = []
    file_system = {
        S: 0,
    }
    for line in read_file(example):
        if line.startswith("$ cd"):
            current_dir = get_current_dir(line[5:], current_dir)
        if line.startswith("$ ls"):
            continue
        if line.startswith("dir "):
            continue
        if "1" <= line[0] <= "9":
            add_to_sum(line, current_dir, file_system)
    print(file_system)
    res = sum_dirs_le(100000, file_system)
    return res


assert main(True) == 95437

print(main())
