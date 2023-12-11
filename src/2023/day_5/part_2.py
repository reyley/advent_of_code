import math

from utils.utils import read_file


class ConversionMap:
    def __init__(self):
        self.map = {}  # (start, end) -> start
        self.keys = []

    def convert(self, value):
        for start, end in self.map:
            if start <= value < end:
                return self.map[(start, end)] + (value - start)
        return value

    def range_end(self, value):
        for start, end in self.map:
            if start <= value < end:
                return end
        if value < self.keys[0][0]:
            return self.keys[0][0]
        if value >= self.keys[-1][1]:
            return math.inf
        for start, end in self.keys:
            if value >= end:
                continue
            else:
                return start

    def len_to_range_end(self, value):
        end = self.range_end(value)
        return end - value

    def add_line(self, line):
        start_dest, start_source, leng = line.split(" ")
        self.add(int(start_source), int(start_source) + int(leng), int(start_dest))

    def add(self, start_source, end_source, start_dest):
        key = (start_source, end_source)
        self.map[key] = start_dest
        self.keys.append(key)
        self.keys.sort()

def parse_seeds(line):
    seeds = [int(v) for v in line.split(" ")]
    seed_ranges = []
    for i in range(0, len(seeds), 2):
        seed_ranges.append((seeds[i], seeds[i] + seeds[i+1]))
    return seed_ranges

def get_location(seed, maps):
    order = ["seed", "soil", "fertilizer", "water", "light", "temperature", "humidity", "location"]
    thing_value = seed
    next_thing_value = None
    print(f"seed: {thing_value}")
    for i, thing in enumerate(order[:-1]):
        next_thing = order[i+1]
        next_thing_value = maps[f"{thing}-to-{next_thing}"].convert(thing_value)
        print(f"{next_thing}: {next_thing_value}")
        thing_value = next_thing_value
    print("")
    return next_thing_value


def get_next(seed, maps):
    order = ["seed", "soil", "fertilizer", "water", "light", "temperature", "humidity", "location"]
    thing_value = seed
    next_thing_value = None
    len_to_end = math.inf
    for i, thing in enumerate(order[:-1]):
        next_thing = order[i+1]
        mp = maps[f"{thing}-to-{next_thing}"]
        next_thing_value = mp.convert(thing_value)
        len_to_end = min(len_to_end, mp.len_to_range_end(thing_value))
        print(f"{next_thing}: {next_thing_value}")
        thing_value = next_thing_value
    print("")
    return seed + len_to_end

def get_min_location(seed_ranges, maps):
    seed_to_loc = consolidate_maps(maps)
    min_location = math.inf
    for seed_range in seed_ranges:
        cur_seed = seed_range[0]
        while cur_seed < seed_range[1]:
            loc = seed_to_loc.convert(cur_seed)
            cur_seed = seed_to_loc.range_end(cur_seed)
            min_location = min(loc, min_location)
    return min_location

def consolidate_maps(maps):
    seed_to_loc = ConversionMap()
    start_seed = 0
    done = False
    while not done:
        start_loc = get_location(start_seed, maps)
        end_seed = get_next(start_seed, maps)
        seed_to_loc.add(start_seed, end_seed, start_loc)
        if end_seed == math.inf:
            done = True
        start_seed = end_seed
    return seed_to_loc


def main(example=False):
    seeds = []
    maps = {}
    current_map: ConversionMap = None
    for line in read_file(example):
        if line.startswith("seeds: "):
            seeds = parse_seeds(line.split("seeds: ")[1])
        elif " map:" in line:
            current_map = ConversionMap()
            maps[line.split(" map:")[0]] = current_map
        elif line:
            current_map.add_line(line)

    res = get_min_location(seeds, maps)
    print(res)
    return res


assert main(True) == 46
main()
