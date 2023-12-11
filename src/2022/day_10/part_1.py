from utils.utils import read_file


def main(example=False):
    x = [1]
    for line in read_file(example):
        x.append(x[-1])
        if line == "noop":
            continue
        n = int(line.split(" ")[-1])
        x.append(n + x[-1])

    print(x)
    res = sum(i * x[i-1] for i in [20, 60, 100, 140, 180, 220])
    print(res)
    return res


assert main(True) == 13140
print(main())
