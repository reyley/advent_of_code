from utils.utils import read_file


def main(example=False):
    res = 0
    for line in read_file(example):
        print(line)
    return res


assert main(True) == 123
print(main())
