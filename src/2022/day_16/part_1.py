from utils.utils import read_file


def get_max_pressure(valve_path, valve_flow, prev_open, current_locations, n_left, mem={}, path=None):
    if not path:
        path = []
    new_path = path
    key = (frozenset(prev_open), frozenset(current_locations), n_left)
    my_location, e_location = current_locations
    r, p = mem.get(key, (None, None))
    if r is not None:
        return r, p
    # print(prev_open, current_locations, n_left)
    if n_left <= 1 or len(prev_open) == len(valve_flow):
        return 0, path

    my_flow = valve_flow.get(my_location, 0)
    e_flow = valve_flow.get(e_location, 0)
    m = 0
    # E Moves I open
    if my_flow != 0 and my_location not in prev_open and n_left > 1:
        for new_e_location in valve_path[e_location]:
            new_prev_open = prev_open.union({my_location})
            temp_path = path + [f"I open {my_location}: {my_flow}, E {e_location} - > {new_e_location}"]
            locations = (my_location, new_e_location)
            partial_pressure, temp_path = get_max_pressure(valve_path, valve_flow, new_prev_open, locations, n_left - 1, mem, temp_path)
            pressure = my_flow * (n_left - 1) + partial_pressure
            if pressure > m:
                new_path = temp_path
                m = pressure

    ## E Moves I Move
    for new_e_location in valve_path[e_location]:
        for new_my_location in valve_path[my_location]:
            temp_path = path + [f"I {my_location} -> {new_my_location}, E {e_location} -> {new_e_location}"]
            v = (new_my_location, new_e_location)
            partial_pressure, temp_path = get_max_pressure(valve_path, valve_flow, prev_open, v, n_left - 1, mem, temp_path)
            if partial_pressure > m:
                new_path = temp_path
                m = partial_pressure

    ## E Opens I Open

    if my_flow != 0 and my_location not in prev_open and n_left > 1:
        if e_flow != 0 and e_location not in prev_open and n_left > 1 and my_location != e_location:
            new_prev_open = prev_open.union({my_location, e_location})
            temp_path = path + [f"I open {my_location}: {my_flow}, E open {e_location}: {e_flow}"]
            partial_pressure, temp_path = get_max_pressure(valve_path, valve_flow, new_prev_open, current_locations, n_left - 1, mem, temp_path)
            pressure = (my_flow + e_flow) * (n_left - 1) + partial_pressure
            if pressure > m:
                new_path = temp_path
                m = pressure

    ## E Opens I Move

    if e_flow != 0 and e_location not in prev_open and n_left > 1:
        for new_my_location in valve_path[my_location]:
            new_prev_open = prev_open.union({e_location})
            temp_path = path + [f"I {my_location} -> {new_my_location}, E open {e_location}: {e_flow}"]
            locations = (new_my_location, e_location)
            partial_pressure, temp_path = get_max_pressure(valve_path, valve_flow, new_prev_open, locations, n_left - 1, mem, temp_path)
            pressure = e_flow * (n_left - 1) + partial_pressure
            if pressure > m:
                new_path = temp_path
                m = pressure

    mem[key] = [m, new_path]
    if m == 1706:
        print(new_path)
    return m, new_path


def get_total_max_pressure(valve_path, valve_flow, n):
    start = "AA", "AA"
    return get_max_pressure(valve_path, valve_flow, set(), start, n)[0]


def main(example=False):
    valve_flow = {}
    valve_path = {}
    for line in read_file(example):
        start, valves = line.replace(",", "").split("; ")
        valves = valves.split(" ")[4:]
        valve, flow = start[6:].split(" has flow rate=")
        flow = int(flow)
        print(valve, flow, valves)
        if flow > 0:
            valve_flow[valve] = flow
        valve_path[valve] = valves

    res = get_total_max_pressure(valve_path, valve_flow, 26)
    print(res)
    return res


# assert main(True) == 1707
print(main())
