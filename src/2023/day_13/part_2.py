from utils.utils import read_file

def find_one_diff(row1, row2):
    has_one_diff = False
    for i in range(len(row1)):
        if row1[i] == row2[i]:
            continue
        elif not has_one_diff:
            has_one_diff = True
        else:
            return False
    return has_one_diff

def get_new_reflection_idx(rows):
    for i in range(1,len(rows)):
        has_one_diff = False
        everything_else_same = False
        for j in range(min(i, len(rows) - i)):
            everything_else_same = True
            if rows[i + j] == rows[i - 1 - j]:
                continue
            elif not has_one_diff and find_one_diff(rows[i + j], rows[i - 1 - j]):
                has_one_diff = True
            else:
                everything_else_same = False
                break
        if everything_else_same and has_one_diff:
            return i
    return None


def get_score(rows, columns):
    score2 = get_new_reflection_idx(rows)
    score1 = get_new_reflection_idx(columns)
    print(score1, score2)
    if score2 and score1:
        print(score1, score2)
    if score2:
        return score2 * 100
    return score1
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


assert main(True) == 400
main()
