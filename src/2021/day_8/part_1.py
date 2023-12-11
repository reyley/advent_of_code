from utils.utils import read_file


def main(example=False):
    s = 0
    for line in read_file(example):
        numbers = line.split(" | ")[1].split(" ")
        for n in numbers:
            if len(n) in [2,3,4,7]:
                s += 1
    res = s
    print(res)
    return res


assert main(True) == 26
main()
