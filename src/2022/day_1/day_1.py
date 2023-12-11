
n = 3
max_n = [0 for x in range(n)]


def collect(current_cal):
    min_ = min(max_n)
    if current_cal > min_:
        max_n.append(current_cal)
        max_n.remove(min_)


with open("input") as f:
    current_cals = 0
    for line in f.readlines():
        line = line.strip()
        print(line)
        if line == "":
            collect(current_cals)
            current_cals = 0
        else:
            current_cals += int(line)
    max_cals = sum(max_n)
    print(max_cals)
