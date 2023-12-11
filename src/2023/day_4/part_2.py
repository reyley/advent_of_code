from utils.utils import read_file


def main(example=False):
    copies = {}
    res = 0
    for i, line in enumerate(read_file(example)):
        _, cards = line.split(": ")
        winning, yours = line.split(" | ")
        winning = set( w for w in winning.split(" ") if w.strip())
        yours = set( w for w in yours.split(" ") if w.strip())
        win_num = len(yours.intersection(winning))
        res += copies.get(i, 0) + 1
        for j in range(win_num):
            copies[i + j + 1] = ( copies.get(i + j + 1, 0) + copies.get(i, 0) + 1 )
    print(res)
    return res


assert main(True) == 30
main()
