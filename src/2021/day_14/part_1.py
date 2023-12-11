from utils.utils import read_file
from collections import Counter

def run_steps(first_line, key_map, n):
    line = first_line
    new_line = []
    for _ in range(n):
        new_line = []
        for i in range(len(line) - 1):
            new_key = key_map[line[i] + line[i + 1]]
            new_line.extend([line[i], new_key])
        new_line.append(line[-1])
        line = new_line
    return new_line

def calculate(new_line):
    counter = Counter(new_line)
    x = counter.most_common()
    return x[0][1] - x[-1][1]


def main(example=False):
    first_line = None
    key_map = {}
    for i, line in enumerate(read_file(example)):
        if i == 0:
            first_line = list(line)
        elif line:
            key, value = line.split(" -> ")
            key_map[key] = value
    n = 10 if example else 10
    new_line = run_steps(first_line, key_map, n)

    res = calculate(new_line)
    print(res)
    return res


assert main(True) == 1588
main()
