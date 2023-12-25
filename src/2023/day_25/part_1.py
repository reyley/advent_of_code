from collections import defaultdict
import numpy as np

from ortools.graph.python import max_flow

from utils.utils import *


def apply(nodes, n=3):
    if n == 0:
        return
    start_nodes_arr = []
    end_nodes_arr = []
    for n1 in nodes:
        for n2 in nodes[n1]:
            start_nodes_arr.append(n1)
            end_nodes_arr.append(n2)

    smf = max_flow.SimpleMaxFlow()

    start_nodes = np.array(start_nodes_arr)
    end_nodes = np.array(end_nodes_arr)
    capacities = np.array([1]*len(start_nodes))
    smf.add_arcs_with_capacity(start_nodes, end_nodes, capacities)
    for i in range(1, len(nodes)):
        smf.solve(0, i)
        if smf.optimal_flow() == n:
            return len(smf.get_source_side_min_cut()) * len(smf.get_sink_side_min_cut())


def main(example=False):
    nodes = defaultdict(set)
    for line in read_file(example):
        start, next_ = line.split(": ")
        other_nodes = next_.split()
        for n in other_nodes:
            nodes[start].add(n)
            nodes[n].add(start)
    node_names = {}
    for i, name in enumerate(nodes):
        node_names[name] = i
    nodes_nums = {}
    for name in nodes:
        nodes_nums[node_names[name]] = {node_names[n] for n in nodes[name]}

    res = apply(nodes_nums)
    print(res)
    return res


assert main(True) == 54
main()
