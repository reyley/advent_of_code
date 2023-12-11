from utils.utils import read_file


def parse(line, phrase):
    if line.startswith(phrase):
        return int(line.split(phrase)[1].strip())
    return 0


def main(example=False):
    x = 0
    y = 0
    for line in read_file(example):
        x += parse(line, "forward")
        y += parse(line, "down")
        y -= parse(line, "up")
    res = x * y
    print(res)
    return res


assert main(True) == 150
main()
