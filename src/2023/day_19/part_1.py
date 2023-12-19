from utils.utils import *

rules = None

comp_func_map = {
    "<": int.__lt__,
    ">": int.__gt__
}

class Func:
    def __init__(self, step):
        self.cond = None
        if ":" in step:
            self.cond, self.result = step.split(":")
            self.key = self.cond[0]
            self.comparison = comp_func_map[self.cond[1]]
            self.num = int(self.cond[2:])
        else:
            self.result = step

    def call(self, elem):
        if self.cond:
            if not self.comparison(elem.get(self.key), self.num):
                return None
        return self.result if self.result in ["R", "A"] else Rule.rules[self.result].call(elem)

class Rule:
    rules = None
    def __init__(self, line):
        self.line = line
        self.name, steps = line.split("{")
        steps = steps[:-1].split(",")
        self.step_funcs = []
        for step in steps:
            self.step_funcs.append(Func(step))
        self.rules[self.name] = self

    def call(self, elem):
        for f in self.step_funcs:
            res = f.call(elem)
            if res is not None:
                return res
        print(elem, self.line)
        assert False

def parse_input(line, incoming):
    elem = {}
    parts = line[1:-1].split(",")
    for part in parts:
        k,v = part.split("=")
        elem[k] = int(v)
    incoming.append(elem)


def main(example=False):
    incoming = []
    Rule.rules = {}
    for line in read_file(example):
        if line and line[0] == "{":
            parse_input(line, incoming)
        elif line:
            Rule(line)

    res = 0
    for inc in incoming:
        if Rule.rules["in"].call(inc) == "A":
            res += sum(inc.values())
    print(res)
    return res


assert main(True) == 19114
main()
