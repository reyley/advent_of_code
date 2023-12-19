from utils.utils import *
from copy import deepcopy

class Func:
    def __init__(self, step):
        self.cond = None
        self.range = None
        if ":" in step:
            self.cond, self.result = step.split(":")
            self.key = self.cond[0]
            self.comparison = self.cond[1]
            self.num = int(self.cond[2:])
            if self.comparison == "<":
                self.yes_range = set(range(1, self.num))
                self.no_range = set(range(self.num, 4001))
            else:
                self.yes_range = set(range(self.num + 1, 4000 + 1))
                self.no_range = set(range(1, self.num + 1))
        else:
            self.result = step

    def call(self, elem):
        if self.cond:
            if not self.comparison(elem.get(self.key), self.num):
                return None
        return self.result if self.result in ["R", "A"] else Rule.rules[self.result].call(elem)

class Rule:
    rules = None
    accept_conditions = None
    def __init__(self, line):
        self.line = line
        self.name, steps = line.split("{")
        steps = steps[:-1].split(",")
        self.step_funcs = []
        for step in steps:
            self.step_funcs.append(Func(step))
        self.rules[self.name] = self

    def call(self, conditions):
        for f in self.step_funcs:
            if f.cond:
                if f.result != "R":
                    yes_cond = deepcopy(conditions)
                    yes_cond[f.key] = conditions[f.key].intersection(f.yes_range)
                    if f.result == "A" and yes_cond[f.key]:
                        self.accept_conditions.append(yes_cond)
                    elif yes_cond[f.key]:
                        Rule.rules[f.result].call(yes_cond)
                no_cond = deepcopy(conditions)
                no_cond[f.key] = conditions[f.key].intersection(f.no_range)
                conditions = no_cond
                if no_cond[f.key]:
                    continue
                else:
                    return
            elif f.result == "A":
                self.accept_conditions.append(conditions)
                return
            elif f.result != "R":
                Rule.rules[f.result].call(conditions)
                return
            elif f.result == "R":
                return

        print(self.line)
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
    Rule.accept_conditions = []
    for line in read_file(example):
        if line and line[0] == "{":
            parse_input(line, incoming)
        elif line:
            Rule(line)

    conditions = {x: set(range(1,4001)) for x in ["x", "m", "a", "s"]}
    Rule.rules["in"].call(conditions)
    res = 0
    for condition in Rule.accept_conditions:
        s = 1
        for k in condition:
            s *= len(condition[k])
        res += s
    print(res)
    return res


assert main(True) == 167409079868000
main()
