from utils.utils import read_file

def get_ops():
    def plus(a,b):
        return a+b
    def minus(a,b):
        return a-b
    def mul(a,b):
        return a*b
    def div(a,b):
        return a/b
    return {
        "+": plus,
        "-": minus,
        "*": mul,
        "/": div
    }


def func(defs, input, ops):
    assert input is not None
    if isinstance(input, int):
        return input
    else:
        op = ops[input[1]]
        arg1 = func(defs, defs.get(input[0]), ops)
        arg2 = func(defs, defs.get(input[2]), ops)
        return op(arg1, arg2)


def main(example=False):
    funcs = {}
    ops = get_ops()
    for line in read_file(example):
        print(line)
        name, func_def = line.split(": ")
        try:
            i = int(func_def)
            funcs[name] = i
        except Exception:
            funcs[name] = func_def.split(" ")

    res = func(funcs, funcs.get("root"), ops)
    print(res)
    return res


assert main(True) == 152
print(main())
