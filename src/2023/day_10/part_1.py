from utils.utils import read_file


def main(example=False):
    for line in read_file(example):
        pass
    res = 0
    print(res)
    return res


assert main(True) == 8
main()
