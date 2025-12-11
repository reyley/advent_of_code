from utils.utils import *
from itertools import combinations

class Machine:
    def __init__(self, final_state, buttons):
        self.final_state = final_state
        self.buttons = buttons

    def fewest_config(self):
        for i in range(1, len(self.buttons)):
            for x in combinations(self.buttons, i):
                if self.set_xor(x) == self.final_state:
                    return i
        assert False

    def set_xor(self, sets):
        cur = set()
        for x in sets:
            for e in x:
                if e in cur:
                    cur.remove(e)
                else:
                    cur.add(e)
        return cur

def main(example=False):
    machines = []
    for line in read_file(example):
        final_state, rest = line.split("] ")
        final_state = final_state.strip("[")
        final_state_set = set()
        for i, ch in enumerate(final_state):
            if ch == "#":
                final_state_set.add(i)
        buttons_str, joltage = rest.split(" {")
        buttons_str = buttons_str.split(" ")
        buttons = []
        for b in buttons_str:
            b = b.strip("()")
            buttons.append(set(int_line(b)))
        machines.append(Machine(final_state_set, buttons))

    res = sum(b.fewest_config() for b in machines)
    print(res)
    return res


assert main(True) == 7
main()