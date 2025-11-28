from utils.utils import *

def is_group(connections, group):
    final_group: set = group.copy()
    for k in group:
        final_group.intersection_update(connections[k])
        if final_group != group:
            return False
    return True

def get_largest_group_for_k(k,connections, n=1):
    if is_group(connections, connections[k]):
        return connections[k]
    else:
        for j in connections[k]:
            copy_k = connections[k].copy()
            copy_k.remove(j)
            if is_group(connections, copy_k):
                return copy_k
    return set()



def main(example=False):
    connections = defaultdict(set)

    for line in read_file(example):
        part1, part2 = line.split("-")
        connections[part1].add(part2)
        connections[part1].add(part1)
        connections[part2].add(part1)
        connections[part2].add(part2)
    for k in connections:
        print(k, connections[k])
    res_group = set()
    for k in connections:
        group = get_largest_group_for_k(k, connections)
        if len(group) > len(res_group):
            res_group = group
    res = ",".join(sorted(res_group))
    print(res)
    return res


assert main(True) == "co,de,ka,ta"
main()
