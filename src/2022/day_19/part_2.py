import datetime

from utils.utils import read_file

material_map = {
    "ore": 0,
    "clay": 1,
    "obsidian": 2,
    "geode": 3
}

def parse_line(line):
    costs = []
    line = line.split('costs ')
    for i in range(1, 5):
        part = line[i].split('.')[0]
        clauses = part.split(' and ')
        cost_dict = {}
        for clause in clauses:
            material = clause.split(' ')[1]
            cost_dict[material_map[material]] = int(clause.split(' ')[0])
        costs.append(cost_dict)
    return costs


def mine(robots, resources):
    new_resources = [0] * 4
    for i in range(4):
        new_resources[i] = resources[i] + robots[i]
    return new_resources


def check_price(robot_price, resources):
    for material, amount in robot_price.items():
        if resources[material] < amount:
            return False
    return True


def buy_robot(robot_price, resources):
    new_resources = [0] * 4
    for i in range(4):
        cost = robot_price.get(i, 0)
        new_resources[i] = resources[i] - cost
    return new_resources


def check_should_only_mine(blueprint, resources, robots):
    for robot_price in blueprint:
        for j in robot_price:
            cost = robot_price[j]
            if cost > 0 and resources[j] < cost and robots[j] > 0:
                return True
    return False

def steps_to_get(cur, r, max_g):
    g = max_g - cur
    i = 0
    while g > 0:
        g - i*r
        i += 1
    return i

def recursive_shenanigans(blueprint, robots, resources, steps_left, maxes, max_geodes):

    if steps_left == 0:
        # if resources[3] == 6:
        #     print(robots, resources)
        return resources[3]

    ans_idle = resources[3] + steps_left*robots[3]
    if ans_idle > max_geodes["n"] and ans_idle > 5:
        print(f"new max: {resources[3] + steps_left*robots[3]}")
        print(robots, resources, steps_left)

    if ans_idle + (steps_left * (steps_left - 1)) / 2 <= max_geodes["n"]:
        return resources[3]

    # if robots[3] == 0:
    #     i = 0
    #     while i > 0:
    #         if resources[2] + i * robots[2] + (i * (i - 1)) / 2 > blueprint[3].get(2, 0)
    #         steps_left_to_build_robot = i

    should_only_mine = check_should_only_mine(blueprint, resources, robots)
    bought_robot = False
    for i in [3,2,1,0]:
        robot_price = blueprint[i]
        if not check_price(robot_price, resources):
            continue
        if robots[i] >= maxes[i] or (i in [1,2] and resources[i] > maxes[i]*1.5):
            continue
        bought_robot = True
        new_resources = buy_robot(robot_price, resources)
        new_resources = mine(robots, new_resources)
        new_robots = robots.copy()
        new_robots[i] += 1
        num_geodes = recursive_shenanigans(blueprint, new_robots, new_resources, steps_left - 1, maxes, max_geodes)
        max_geodes["n"] = max(max_geodes["n"], num_geodes)

    if should_only_mine or not bought_robot:
        new_resources = mine(robots, resources)
        new_robots = robots.copy()
        num_geodes = recursive_shenanigans(blueprint, new_robots, new_resources, steps_left - 1, maxes, max_geodes)
        max_geodes["n"] = max(max_geodes["n"], num_geodes)
    return max_geodes["n"]


def get_maxes(cost_list):
    maxes = [1000000]*4
    for i in range(3):
        maxes[i] = max(x[i] for x in cost_list if i in x)
    print(maxes)
    return maxes


def main(example=False):
    res = 1
    tstart = datetime.datetime.now()
    for i, line in enumerate(read_file(example)):
        start = datetime.datetime.now()
        if i >= 3:
            break
        cost_list = parse_line(line)
        print(cost_list)
        maxes = get_maxes(cost_list)
        geodes = recursive_shenanigans(cost_list, [1, 0, 0, 0], [0] * 4, 32, maxes, {"n": 0})
        res *= geodes
        print(geodes, datetime.datetime.now() - start)

    print(res, datetime.datetime.now() - tstart)
    return res


assert main(True) == 62 * 56
print(main())
