from utils.utils import read_file


def check_adjacent(i, j, lines):
    gears = set()
    for offset_i in [-1, 0, 1]:
        for offset_j in [-1, 0, 1]:
            new_i, new_j = i + offset_i, j + offset_j
            if new_i < 0 or new_i >= len(lines) :
                continue
            if new_j < 0 or new_j >= len(lines[new_i]) :
                continue
            char = lines[new_i][new_j]
            if char == "*":
                gears.add((new_i,new_j))
    return gears


def sum_lines(lines):
    gear_map = {}
    for i, line in enumerate(lines):
        print(line)
        num = ""
        gears = set()
        for j, char in enumerate(line):
            if char.isnumeric():
                num += char
                gears.update(check_adjacent(i, j, lines))
            elif num:
                if gears:
                    for g in gears:
                        gear_map[g] = {int(num)}.union(gear_map.get(g, set()))
                num = ""
                gears = set()
        if num and gears:
            for g in gears:
                gear_map[g] = {int(num)}.union(gear_map.get(g, set()))
    s = 0
    for g, nums in gear_map.items():
        if len(nums) == 2:
            s += nums.pop()*nums.pop()
    return s

def main(example=False):
    lines = []
    for line in read_file(example):
        print(line)
        lines.append(line)
    res = sum_lines(lines)
    print(res)
    return res


# assert main(True) == 467835
main()
