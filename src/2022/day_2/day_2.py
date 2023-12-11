
them_ = ["A", "B", "C"]
you_ = ["X", "Y", "Z"]

points_map = {
    "X": 0,
    "Y": 3,
    "Z": 6
}

RPC_MAP = {
    "AX": 2,
    "BX": 3,
    "CX": 1,
    "AY": 1,
    "BY": 2,
    "CY": 3,
    "AZ": 3,
    "BZ": 1,
    "CZ": 2,
}

score = 0


def points(you, them):
    p = points_map[you] + 1
    i = them_.index(them)
    if you == "Y":
        return p + i
    if you == "X":
        return p + (i - 1) % 3
    if you == "Z":
        return p + (i + 1) % 3


def main():
    global score
    with open("input") as f:
        for l in f:
            them, _, you = l.strip()
            # print(score)
            score += points(you, them)
    print(score)

main()
