from utils.utils import read_file


class ConversionMap:
    def __init__(self):
        self.map = {}  # (start, end) -> start

    def convert(self, value):
        for start, end in self.map:
            if start <= value < end:
                return self.map[(start, end)] + (value - start)
        return value

    def add(self,line):
        start_dest, start_source, leng = line.split(" ")
        self.map[(int(start_source), int(start_source) + int(leng))] = int(start_dest)

def parse_seeds(line):
    return [int(v) for v in line.split(" ")]

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


def get_min_location(seeds, maps):
    min_location = None
    for seed in seeds:
        loc = get_location(seed, maps)
        if min_location is None:
            min_location = loc
        else:
            min_location = min(loc, min_location)
    return min_location


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
            current_map.add(line)

    res = get_min_location(seeds, maps)
    print(res)
    return res


assert main(True) == 35
main()
