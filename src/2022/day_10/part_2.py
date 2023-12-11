from utils.utils import read_file


def main(example=False):
    x = [1]
    pix = []
    for line in read_file(example):
        x.append(x[-1])
        if line == "noop":
            continue
        n = int(line.split(" ")[-1])
        x.append(n + x[-1])

    print(x)
    print(len(x))
    for i in range(len(x)):
        print(x[i], i)
        if abs(x[i] - i % 40) <= 1:
            pix.append('#')
        else:
            pix.append(".")
        print(pix[-1])
    print(pix)
    res = ["".join(pix[i:i + 40]) for i in [0, 40, 80, 120, 160, 200]]
    for _ in res:
        print(_)
    print(res)
    return res

print(main())
