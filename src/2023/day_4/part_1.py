from utils.utils import read_file


def main(example=False):
    res = 0
    for line in read_file(example):
        _, cards = line.split(": ")
        winning, yours = line.split(" | ")
        winning = set( w for w in winning.split(" ") if w.strip())
        yours = set( w for w in yours.split(" ") if w.strip())
        pow = len(yours.intersection(winning))
        if pow:
            res += 2 ** (pow - 1)
    print(res)
    return res


assert main(True) == 13
main()
