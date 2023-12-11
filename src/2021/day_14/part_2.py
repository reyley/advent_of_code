from utils.utils import read_file
from collections import Counter

def run_steps(first_line, key_map, n):
    line = Counter([first_line[i] + first_line[i + 1] for i in range(len(first_line) - 1)])
    new_line = Counter()
    for _ in range(n):
        new_line =  Counter()
        for pair, c in line.items():
            new_key = key_map[pair]
            new_line[pair[0] + new_key] += c
            new_line[new_key + pair[1]] += c
        line = new_line
    return new_line

def calculate(new_line, first_line):
    counter = Counter()
    for k,v in new_line.items():
        counter[k[0]] += v
    counter.update(first_line[-1])
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
    n = 40
    new_line = run_steps(first_line, key_map, n)

    res = calculate(new_line, first_line)
    print(res)
    return res


assert main(True) == 2188189693529
main()
