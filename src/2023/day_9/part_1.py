from utils.utils import read_file

def get_next(seq):
    lasts = [seq[-1]]
    while not all(x == 0 for x in seq):
        next_seq = []
        for i in range(len(seq) - 1):
            next_seq.append(seq[i+1] - seq[i])
        lasts.append(next_seq[-1])
        seq = next_seq
    return sum(lasts)

def main(example=False):
    res = 0
    for line in read_file(example):
        res += get_next([int(x) for x in line.split(" ")])
    print(res)
    return res


assert main(True) == 114
main()
