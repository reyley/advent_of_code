from utils.utils import *

class Gate:
    values = {}
    gates: list["Gate"] = []
    def __init__(self, a, b, t, o):
        self.a = a
        self.b = b
        self.f = self.get_f(t)
        self.o = o
        self.done = False

    def get_f(self, t):
        if t == "AND":
            return lambda x, y: x&y
        if t == "OR":
            return lambda x, y: x|y
        if t == "XOR":
            return lambda x, y: x^y

    def run(self):
        if self.a in self.values and self.b in self.values:
            self.values[self.o] = self.f(self.values[self.a], self.values[self.b])
            self.done = True

def main(example=False):
    Gate.values = {}
    Gate.gates = []
    for line, part in read_split_file(example):
        if part == 1:
            k, v = line.split(": ")
            Gate.values[k] = int(v)
        if part == 2:
            line_s = line.split(" ")
            gate = Gate(line_s[0], line_s[2], line_s[1], line_s[4])
            gate.gates.append(gate)
    Gate.values[f"x00"] = 0
    Gate.values[f"y00"] = 1
    for i in range(1, 100):
        Gate.values[f"x{i:02d}"] = 0
        Gate.values[f"y{i:02d}"] = 0
    all_done = False
    while not all_done:
        all_done = True
        for g in Gate.gates:
            if not g.done:
                all_done = False
                g.run()
    num = 0
    for i in range(100):
        b = Gate.values.get(f"z{i:02d}", 0)
        num += b*(2**i)


    res = num
    print(res)
    return res


assert main(True) == 2024
main()
