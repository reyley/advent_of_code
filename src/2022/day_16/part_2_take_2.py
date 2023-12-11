from utils.utils import read_file


def add_pressure(valve_path, valve_flow, paths, prev_open, current_locations, n_left, pressure_until_now):
    step_pressure = sum(valve_flow[v] for v in prev_open)
    if n_left <= 1 or len(prev_open) == len(valve_flow):
        p = pressure_until_now + n_left*step_pressure
        key = frozenset(prev_open)
        if key not in paths or paths[key] < p:
            paths[key] = p
        return

    v_options = valve_path[current_locations]

    if current_locations not in prev_open:
        p = pressure_until_now + step_pressure
        _prev_open = prev_open | {current_locations}
        add_pressure(valve_path, valve_flow, paths, _prev_open, current_locations, n_left - 1, p)
    else:
        for v in v_options:
            v_n = v_options[v]
            if v_n < n_left and v not in prev_open:
                p = pressure_until_now + v_n*step_pressure
                add_pressure(valve_path, valve_flow, paths, prev_open, v, n_left - v_n, p)

    p = pressure_until_now + n_left * step_pressure
    key = frozenset(prev_open)
    if key not in paths or paths[key] < p:
        paths[key] = p


def min_steps(valve_path, s_valve, e_valve, mem, in_path=None):
    if in_path is None:
        in_path = {s_valve}
    key = (s_valve, e_valve)
    if key in mem:
        return mem[key]
    if e_valve in valve_path[s_valve]:
        mem[key] = 1, {s_valve, e_valve}
        return mem[key]
    min_path_l = None
    min_path = None
    for v in valve_path[s_valve]:
        if v not in in_path:
            r_l, r_path = min_steps(valve_path, v, e_valve, mem, in_path | {v})
            if r_l is None and r_path is None:
                continue
            p = 1 + r_l
            if min_path_l is None or p < min_path_l:
                min_path_l = p
                min_path = in_path | r_path
    if min_path is None:
        return None, None
    mem[key] = min_path_l, min_path
    return mem[key]


def get_weighted_valve_path(valve_path, valves):
    new_valve_path = {v: {} for v in valves}
    mem = {}
    for s_valve in valves:
        for e_valve in valves:
            new_valve_path[s_valve][e_valve] = min_steps(valve_path, s_valve, e_valve, mem)[0]
    print(new_valve_path)
    return new_valve_path


def get_pressures_from(paths, loc, valve_path, w_valve_path, valve_flow, n_steps, been):
    if loc in been:
        return
    been.add_line(loc)
    for x in valve_path[loc]:
        if x in w_valve_path:
            add_pressure(w_valve_path, valve_flow, paths, set(), x, n_steps - 1, 0)
        else:
            get_pressures_from(paths, x, valve_path, w_valve_path, valve_flow, n_steps - 1, been)


def get_total_pressure(valve_path, w_valve_path, valve_flow, n_steps):
    start = "AA"
    paths = {}
    get_pressures_from(paths, start, valve_path, w_valve_path, valve_flow, n_steps, set())
    print(paths)
    return paths


def get_mex_2_paths(paths):
    m = 0
    for path, l in paths.items():
        for e_path, e_l in paths.items():
            if e_path & path:
                continue
            if l + e_l > m:
                m = l + e_l
    print(m)
    return m


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

    w_valve_path = get_weighted_valve_path(valve_path, valve_flow.keys())
    print(valve_path)
    paths = get_total_pressure(valve_path, w_valve_path, valve_flow, 26)
    res = get_mex_2_paths(paths)
    print(res)
    return res


assert main(True) == 1707
print(main())
