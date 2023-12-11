from utils.utils import read_file

material_map = {
    "ore": 0,
    "clay": 1,
    "obsidian": 2,
    "geode": 3
}


def move_line(i, file: list):
    line = file.pop(i)
    new_i = (i + line[0]) % len(file)
    line[1] = True
    if new_i == 0:
        file.append(line)
    else:
        file.insert(new_i, line)


def move(file):
    i = 0
    while i < len(file):
        if file[i][1]:
            i += 1
        else:
            move_line(i, file)


def get(file, n, idx_n):
    n = file.index([idx_n, True]) + n
    return file[n % len(file)][0]


def main(example=False):
    file = []
    for line in read_file(example):
        file.append([int(line), False])
    move(file)
    res = get(file, 1000,0) + get(file, 2000,0) + get(file, 3000,0)
    print(res)
    return res


assert main(True) == 3
print(main())
