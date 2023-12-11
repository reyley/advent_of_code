from utils.utils import read_file

def get_steps(step_map, seq):
    key = "AAA"
    step = 0
    while key != "ZZZ":
        side = int(seq[step % len(seq)])
        key = step_map[key][side]
        step += 1
    return step


def main(example=False):
    step_map = {}
    seq = ""
    for line in read_file(example):
        if "=" in line:
            key, value = line.strip(")").split(" = (")
            step_map[key] = value.split(", ")
        elif line:
            seq = line.replace("L", "0").replace("R", "1")
    res = get_steps(step_map, seq)
    print(res)
    return res


assert main(True) == 6
main()
