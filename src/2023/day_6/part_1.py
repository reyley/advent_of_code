from functools import cache

from utils.utils import read_file

def parse(line):
    return [int(num) for num in line.split(" ") if num]

@cache
def distance(time_press, time):
    return (time - time_press)*time_press

def num_wins(time, dis):
    wins = 0
    for i in range(1,time):
        if distance(i, time) > dis:
            wins += 1
    return wins

def get_res(times, distances):
    res = 1
    for time, dis in zip(times, distances):
        res *= num_wins(time, dis)
    return res

def main(example=False):
    times = []
    distances = []
    for line in read_file(example):
        if line.startswith("Time:"):
            times = parse(line.split("Time:")[1])
        else:
            distances = parse(line.split("Distance:")[1])
        pass
    res = get_res(times, distances)
    print(res)
    return res


assert main(True) == 288
main()
