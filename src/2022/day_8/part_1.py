from utils.utils import read_file


def main(example=False):
    res = 0
    forest = []
    inverse_forest = []
    visible_trees = set()
    for line in read_file(example):
        forest.append(list(map(lambda x:int(x), line)))
        if not inverse_forest:
            inverse_forest = [[int(i)] for i in line]
        else:
            for i, x in enumerate(list(line)):
                inverse_forest[i].append(int(x))
    print(forest)
    print(inverse_forest)
    for i, row in enumerate(forest):
        max = -1
        for j, tree in enumerate(row):
            if tree > max:
                visible_trees.add((i,j))
                max = tree
                print(tree)
    print(visible_trees)
    for i, row in enumerate(forest):
        max = -1
        for j, tree in enumerate(row[::-1]):
            if tree > max:
                visible_trees.add((i, len(row) - j - 1))
                max = tree
    print(visible_trees)
    for i, row in enumerate(inverse_forest):
        max = -1
        for j, tree in enumerate(row):
            if tree > max:
                visible_trees.add((j, i))
                max = tree
    print(visible_trees)
    for i, row in enumerate(inverse_forest):
        max = -1
        for j, tree in enumerate(row[::-1]):
            if tree > max:
                visible_trees.add((len(row) - j - 1, i))
                max = tree
    print(visible_trees)
    res = len(visible_trees)
    print("example:" if example else "result:", res)
    return res


assert main(True) == 21

print(main())
