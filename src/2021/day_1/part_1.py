from utils.utils import read_file


def main(example=False):
    s = 0
    prev = None
    for line in read_file(example):
        num = int(line)
        if prev is not None and num > prev:
            s += 1
        prev = num
    res = s
    print(res)
    return res


assert main(True) == 7
main()
