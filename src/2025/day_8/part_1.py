import heapq
from math import sqrt

from utils.utils import *
from utils.minheap import MinHeap

class Circuit:
    all = {}
    node_to_circuit = {}
    idx = 0


    def __init__(self, nodes=None):
        self.nodes = set() if nodes is None else nodes
        self.key = self.idx
        self.idx += 1
        Circuit.all[self.key] = self
        for node in self.nodes:
            Circuit.node_to_circuit[node] = self

    def add(self, node):
        self.nodes.add(node)
        Circuit.node_to_circuit[node] = self

    def merge(self, other):
        for node in other.nodes:
            Circuit.node_to_circuit[node] = self
        self.nodes |= other.nodes
        del self.all[other.key]

def distance(box1, box2):
    diff = 0
    for k in range(len(box1)):
        diff += (box1[k] - box2[k])**2
    return sqrt(diff)

def populate_shortest_connections(boxes, shortest_connections):
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            diff = distance(boxes[i], boxes[j])
            if i==0 and j == 19:
                print(f"Distance between {boxes[i]} and {boxes[j]} is {diff}")
            shortest_connections.push((boxes[i], boxes[j]), diff)


def create_circuits(shortest_connections):
    for _connection in shortest_connections.ordered():
        diff, (box1, box2) = _connection
        circuit1 = Circuit.node_to_circuit.get(box1)
        circuit2 = Circuit.node_to_circuit.get(box2)
        if circuit1 and circuit2:
            if circuit1 != circuit2:
                circuit1.merge(circuit2)
        elif circuit1:
            circuit1.nodes.add(box2)
            Circuit.node_to_circuit[box2] = circuit1
        elif circuit2:
            circuit2.nodes.add(box1)
            Circuit.node_to_circuit[box1] = circuit2
        else:
            Circuit({box1, box1})

def main(example=False):
    Circuit.all = {}
    Circuit.node_to_circuit = {}
    boxes = []
    shortest_connections = MinHeap(size=10 if example else 1000)
    for line in read_file(example):
        boxes.append(tuple(int_line(line)))
    populate_shortest_connections(boxes, shortest_connections)
    create_circuits(shortest_connections)
    top_3 = []
    for c in Circuit.all.values():
        if len(top_3) < 3:
            heapq.heappush(top_3, len(c.nodes))
        else:
            heapq.heappushpop(top_3, len(c.nodes))
    res = mul(top_3)
    print(res)
    return res


assert main(True) == 13
main()