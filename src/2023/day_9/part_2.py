from utils.utils import read_file

def get_prev(seq):
    firsts = [seq[0]]
    while not all(x == 0 for x in seq):
        next_seq = []
        for i in range(len(seq) - 1):
            next_seq.append(seq[i+1] - seq[i])
        firsts.append(next_seq[0])
        seq = next_seq
    minus = 0
    for x in firsts[::-1]:
        minus = x - minus
    return minus

def main(example=False):
    res = 0
    for line in read_file(example):
        res += get_prev([int(x) for x in line.split(" ")])
    print(res)
    return res


assert main(True) == 2
main()
