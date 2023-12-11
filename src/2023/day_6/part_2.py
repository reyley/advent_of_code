from functools import cache

from utils.utils import read_file

def parse(line):
    return int(line.replace(" ", ""))

@cache
def distance(time_press, time):
    return (time - time_press)*time_press

def num_wins(time, dis):
    wins_start = 0
    wins_end = None
    for i in range(1,time):
        if distance(i, time) > dis:
            wins_start = i
            break
    for i in range(time, wins_start, -1):
        if distance(i, time) > dis:
            wins_end = i
            break
    return wins_end - wins_start + 1

def main(example=False):
    for line in read_file(example):
        if line.startswith("Time:"):
            time = parse(line.split("Time:")[1])
        else:
            distance = parse(line.split("Distance:")[1])
        pass
    res = num_wins(time, distance)
    print(res)
    return res


assert main(True) == 71503
main()
