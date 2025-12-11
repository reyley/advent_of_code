from utils.utils import *
from itertools import combinations

class Machine:
    def __init__(self, final_state, buttons, joltage):
        self.final_state = final_state
        self.buttons = buttons
        self.joltage = joltage

    def fewest_config(self):
        for i in range(1, len(self.buttons)):
            for x in combinations(self.buttons, i):
                if self.set_xor(x) == self.final_state:
                    return i
        assert False

    def find_min_joltage(self):
        prev_states = {(0,)*len(self.joltage)}
        cur_states = {(0,)*len(self.joltage)}
        n_buttons = 0
        while True:
            new_states = set()
            n_buttons += 1
            for state in cur_states:
                for b in self.buttons:
                    new_state = self.add_states(b, state)
                    if new_state == self.joltage:
                        return n_buttons
                    if self.is_valid(new_state) and new_state not in prev_states:
                        new_states.add(new_state)
            prev_states = cur_states
            cur_states = new_states

    def set_xor(self, sets):
        cur = set()
        for x in sets:
            for e in x:
                if e in cur:
                    cur.remove(e)
                else:
                    cur.add(e)
        return cur

    def set_counter_match_joltage(self, sets):
        cur = { i:0 for i in self.joltage}
        for x in sets:
            for e in x:
                cur[e] += 1
                if cur[e] > self.joltage[e]:
                    return False
        return cur == self.joltage

    def add_states(self, b, state):
        r = []
        for i, s in enumerate(state):
            x = s + 1 if i in b else s
            r.append(x)
        return tuple(r)

    def is_valid(self, new_state):
        return all(new_state[i] <= self.joltage[i] for i in range(len(new_state)))


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
        joltage = tuple(int_line(joltage.strip("}")))
        machines.append(Machine(final_state_set, buttons, joltage))

    res = sum(b.find_min_joltage() for b in machines)
    print(res)
    return res


assert main(True) == 33
main()