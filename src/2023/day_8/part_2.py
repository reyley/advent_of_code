import math
from functools import cache

from utils.utils import read_file

step_map = {}
seq = ""

def get_keys(end_letter):
    return frozenset(key for key in step_map.keys() if key[-1] == end_letter)

def all_end_in(keys, letter):
    return all(key[-1] == letter for key in keys)

@cache
def next_keys(keys, side):
    new_keys = frozenset(step_map[key][side] for key in keys)
    return new_keys

def find_loop(start_key):
    past_steps = set()
    z_steps = set()
    step = 0
    key = start_key
    while (step % len(seq), key) not in past_steps:
        # print(step, key)
        past_steps.add((step % len(seq), key))
        if key.endswith("Z"):
            z_steps.add((step , key))
            return z_steps, step, len(past_steps)
        side = int(seq[step % len(seq)])
        key = step_map[key][side]
        step += 1
    return z_steps, step, len(past_steps)


def get_steps():
    keys = get_keys("A")
    len_loops = set()
    for key in keys:
        z_steps, len_loop, past_steps = find_loop(key)  # I know z_steps is all at the end of the loop
        len_loops.add(len_loop)
        print(z_steps, len_loop, past_steps)
    res = 1
    return math.lcm(*len_loops)
    # for len_loop in len_loops:
    #     res = int(res * len_loop / math.gcd(res, len_loop))
    # return res



def main(example=False):

    global step_map
    global seq
    step_map = {}
    seq = ""
    for line in read_file(example):
        if "=" in line:
            key, value = line.strip(")").split(" = (")
            step_map[key] = value.split(", ")
        elif line:
            seq = line.replace("L", "0").replace("R", "1")
    print(len(seq))
    res = get_steps()
    print(res)
    return res

# 1656491371898708158316544
# assert main(True) == 6
main()
