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


def get_num(res, arg1, op, arg2):
    i = arg2 if arg1 == "x" else arg1
    if op == "*":
        return res / i
    if op == "+":
        return res - i
    if op == "/":
        if arg1 == "x":
            return res * arg2
        else:
            return arg1 / res
    if op == "-":
        if arg1 == "x":
            return res + arg2
        else:
            return arg1 - res
    if op == "=":
        return i


def func(defs, input, ops, mem):
    assert input is not None
    if isinstance(input, int):
        return input
    if input == "x":
        raise Exception
    else:
        op = ops[input[1]]
        m1, m2 = input[0], input[2]
        arg1 = func(defs, defs.get(m1), ops, mem) if m1 not in mem else mem[m1]
        mem[m1] = arg1
        arg2 = func(defs, defs.get(m2), ops, mem) if m2 not in mem else mem[m2]
        mem[m2] = arg2
        return op(arg1, arg2)


def try_comp(funcs, ops, mem, start, res):
    a, op, b = funcs.get(start)
    arg1, arg2, bad = None, None,  None
    try:
        arg1 = func(funcs, funcs.get(a), ops, mem)
        bad = b
        arg2 = "x"
    except Exception:
        bad = a
        arg1 = "x"
        arg2 = func(funcs, funcs.get(b), ops, mem)
    new_res = get_num(res, arg1, op, arg2)
    if bad == "humn":
        return new_res
    else:
        return try_comp(funcs, ops, mem, bad, new_res)


def main(example=False):
    funcs = {}
    ops = get_ops()
    mem = {}
    for line in read_file(example):
        print(line)
        name, func_def = line.split(": ")
        try:
            if name == "humn":
                funcs[name] = "x"
            else:
                i = int(func_def)
                funcs[name] = i
        except Exception:
            i = func_def.split(" ")
            if name == "root":
                i[1] = "="
            funcs[name] = i

    res = try_comp(funcs, ops, mem, "root", None)
    print(res)
    return res


assert main(True) == 301
print(main())
