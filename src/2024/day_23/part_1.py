from utils.utils import *


def main(example=False):
    ts = set()
    finished_ts = set()
    triplets = set()
    connections = defaultdict(set)
    for line in read_file(example):
        part1, part2 = line.split("-")
        if "t" == part1[0]:
            ts.add(part1)
        if "t" == part2[0]:
            ts.add(part2)
        connections[part1].add(part2)
        connections[part2].add(part1)
    for t in ts:
        for n1 in connections[t]:
            if n1 in finished_ts:
                continue
            for n2 in connections[t]:
                if n2 in finished_ts or n1 == n2 or n1 not in connections[n2]:
                    continue
                triplet = tuple(sorted([n1, t, n2]))
                if triplet not in triplets:
                    print(triplet)
                    triplets.add(triplet)
        finished_ts.add(t)
    res = len(triplets)
    print(res)
    return res


assert main(True) == 7
main()
