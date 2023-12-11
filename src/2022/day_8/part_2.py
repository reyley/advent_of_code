from utils.utils import read_file


def traverse_forest(forest, idx_func, visible_trees, inverse=False):
    for i, row in enumerate(forest):
        row = row[::-1] if inverse else row
        for j, tree in enumerate(row):
            n = 0
            while j-n >= 0 and j > 0:
                n += 1
                if row[j-n] >= tree or j == n:
                    break
            if (idx_func(i,j) == (3,2)):
                print(tree, n)
            visible_trees[idx_func(i,j)] *= n


def main(example=False):
    res = 0
    forest = []
    inverse_forest = []
    # visible_trees = {}
    for line in read_file(example):
        forest.append(list(map(lambda x:int(x), line)))
        if not inverse_forest:
            inverse_forest = [[int(i)] for i in line]
        else:
            for i, x in enumerate(list(line)):
                inverse_forest[i].append(int(x))
    len_row = len(forest[0])
    visible_trees = {(i,j): 1 for i in range(len_row) for j in range(len_row)}
    print(forest)
    print(inverse_forest)
    traverse_forest(forest, lambda i, j: (i, j), visible_trees, inverse=False)
    traverse_forest(forest, lambda i, j: (i, len_row - j - 1), visible_trees, inverse=True)
    traverse_forest(inverse_forest, lambda i, j: (j, i), visible_trees, inverse=False)
    traverse_forest(inverse_forest, lambda i, j: (len_row - j - 1, i), visible_trees, inverse=True)
    print(visible_trees)
    res = max(list(visible_trees.values()))
    print("example:" if example else "result:", res)
    return res


assert main(True) == 8

print(main())
