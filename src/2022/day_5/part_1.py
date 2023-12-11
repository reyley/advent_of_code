



def read_file(example=False):
    file = "example" if example else"input"
    with open(file) as f:
        for x in f:
            yield x


def move_cranes(command, cranes):
    if not command.strip():
        return
    command = command[5:]
    print(command)
    n, command = command.split(" from ")
    print(n, command)
    from_, to_ = command.split(" to ")
    print(from_,to_)
    from_, to_ = int(from_), int(to_)
    if to_ not in cranes:
        cranes[to_] = []
    cranes[to_] += cranes[from_][-int(n):]
    cranes[from_] = cranes[from_][:-int(n)]
    print(cranes)


def add_to_crane(chr, idx, cranes):
    crane = ( idx - 1 ) // 4 + 1
    if crane in cranes:
        cranes[crane].append(chr)
    else:
        cranes[crane] = [chr]


def parse_cranes(line, cranes):
    i = 1
    while i < len(line):
        if line[i] != ' ':
            add_to_crane(line[i], i, cranes)
        i += 4


def main(example=False):
    cranes = {}
    parse = True
    for line in read_file(example):
        if len(line) > 1 and line[1] == '1':
            parse = False
            for crane in cranes:
                cranes[crane] = list(reversed(cranes[crane]))
            print(cranes)
            continue
        print(line)
        if parse:
            parse_cranes(line, cranes)
        else:
            move_cranes(line, cranes)
    res = ''
    for i in range(max(cranes.keys()) + 1):
        if i in cranes and cranes[i]:
            res += cranes[i][-1]
        else:
            res += ' '
    return res.strip()


assert main(True) == 'MCD'
print(main())
