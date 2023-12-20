from utils.utils import *



class ModuleType:
    flipflop = 0
    broadcaster = 1
    conjunction = 2

class Module:
    all = None
    def __init__(self, line):
        self.name = None
        self.destinations = []
        self.type = None
        self.is_on = False
        self.prev_call = {}
        self.parse(line)
        self.all[self.name] = self

    def parse(self, line):
        start, dest = line.split(" -> ")
        self.destinations = dest.split(", ")
        if start == "broadcaster":
            self.type = ModuleType.broadcaster
            self.name = start
        elif start[0] == "%":
            self.type = ModuleType.flipflop
            self.name = start[1:]
        elif start[0] == "&":
            self.type = ModuleType.conjunction
            self.name = start[1:]


    def call(self, pulse, prev_func):
        output_pulse = None
        if self.type == ModuleType.broadcaster:
            output_pulse = pulse
        elif self.type == ModuleType.flipflop:
            if pulse == 0:
                output_pulse = 0 if self.is_on else 1
                self.is_on = not self.is_on
        elif self.type == ModuleType.conjunction:
            self.prev_call[prev_func] = pulse
            output_pulse = 1
            if all(v == 1 for x, v in self.prev_call.items()):
                output_pulse = 0
        return [(self.name, f, output_pulse) for f in self.destinations] if output_pulse is not None else []

    def add_caller(self, name):
        if self.type == ModuleType.conjunction:
            self.prev_call[name] = 0

    def __hash__(self):
        hashable_prev = ((k, self.prev_call[k]) for k in sorted(self.prev_call.keys()))
        return hash((self.name, self.is_on, hashable_prev))

    @classmethod
    def state(cls):
        return hash((hash(cls.all[f]) for f in sorted(cls.all.keys())))

    @classmethod
    def register_callers(cls):
        for f in cls.all:
            for dest in cls.all[f].destinations:
                if dest in cls.all:
                    cls.all[dest].add_caller(f)

def run():
    calls = [("button", "broadcaster", 0)]
    n_high = 0
    n_low = 0
    while calls:
        prev,f,p = calls.pop(0)
        if p == 0:
            n_low += 1
        else:
            n_high += 1
        if f in Module.all:
            calls.extend(Module.all[f].call(p, prev))
    return n_low, n_high

def cycle(n):
    total_high = 0
    total_low = 0
    for i in range(n):
        n_high, n_low = run()
        total_low += n_low
        total_high += n_high
    return total_low * total_high

def main(example=False):
    Module.all = {}
    for line in read_file(example):
        Module(line)
    Module.register_callers()

    res = cycle(1000)
    print(res)
    return res


assert main(True) == 11687500
main()
