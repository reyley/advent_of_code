from utils.utils import read_file


def check_adjacent(i, j, lines):
    for offset_i in [-1, 0, 1]:
        for offset_j in [-1, 0, 1]:
            new_i, new_j = i + offset_i, j + offset_j
            if new_i < 0 or new_i >= len(lines) :
                continue
            if new_j < 0 or new_j >= len(lines[new_i]) :
                continue
            char = lines[new_i][new_j]
            if char.isnumeric() or char == ".":
                continue
            else:
                return True
    return False


def sum_lines(lines):
    s = 0
    for i, line in enumerate(lines):
        print(line)
        num = ""
        adjacent = False
        for j, char in enumerate(line):
            if char.isnumeric():
                num += char
                if not adjacent and check_adjacent(i, j, lines):
                    adjacent = True
            elif num:
                if adjacent:
                    s += int(num)
                num = ""
                adjacent = False
        if num and adjacent:
            s += int(num)
    return s

def main(example=False):
    lines = []
    for line in read_file(example):
        print(line)
        lines.append(line)
    res = sum_lines(lines)
    print(res)
    return res


assert main(True) == 4361
main()
