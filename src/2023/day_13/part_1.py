from utils.utils import read_file


def get_reflection_idx(rows):
    for i in range(1,len(rows)):
        done = False
        for j in range(min(i, len(rows) - i)):
            done = True
            if rows[i + j] != rows[i - 1 - j]:
                done = False
                break
        if done:
            return i
    return None


def get_score(rows, columns):
    i = get_reflection_idx(rows)
    if i is not None:
        return i * 100
    i = get_reflection_idx(columns)
    if i is not None:
        return i
    return 0

def main(example=False):
    rows = []
    columns = []
    res = 0
    for line in read_file(example):
        if not line:
            score = get_score(rows, columns)
            res += score
            rows = []
            columns = []
        else:
            rows.append(list(line))
            for i, ch in enumerate(line):
                if not columns:
                    columns = [[] for _ in range(len(line))]
                columns[i].append(ch)

    score = get_score(rows, columns)
    res += score

    print(res)
    return res


assert main(True) == 405
main()
