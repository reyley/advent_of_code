from utils.utils import read_file


class Elem:
    def __init__(self, n):
        self.n = n * 811589153


def move_line(i, file: list, elems):
    elem = elems[i]
    i = file.index(elem)
    file.pop(i)
    new_i = (i + elem.n) % len(file)
    if new_i == 0:
        file.append(elem)
    else:
        file.insert(new_i, elem)


def move(file, elems):
    for i in range(len(file)):
        move_line(i, file, elems)


def get(file, n, elem):
    n = file.index(elem) + n
    return file[n % len(file)].n


def main(example=False):
    file = []
    elems = {}
    start_elem = 0
    for i, line in enumerate(read_file(example)):
        elem = Elem(int(line))
        if (int(line)) == 0:
            start_elem = elem
        file.append(elem)
        elems[i] = elem
    for i in range(10):
        move(file, elems)
    res = get(file, 1000, start_elem) + get(file, 2000, start_elem) + get(file, 3000, start_elem)
    print(res)
    return res


assert main(True) == 1623178306
print(main())
