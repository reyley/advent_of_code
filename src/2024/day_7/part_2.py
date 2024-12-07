from functools import cache
from typing import Callable

from utils.utils import *


def concat(num1,num2):
    return int(str(num1) + str(num2))


OPS = {
    "*": int.__mul__,
    "+": int.__add__,
    "|": concat
}

@cache
def function_combinations(length) -> set[list[Callable]]:
    prev_res = {"*", "+", "|"}
    for i in range(1, length):
        res = set()
        res.update(x + "*" for x in prev_res)
        res.update(x + "+" for x in prev_res)
        res.update(x + "|" for x in prev_res)
        prev_res = res
    return prev_res


def mul(operands):
    res = 1
    for i in operands:
        res = res * i
    return res



def run(operators, operands):
    res = None
    for i in range(len(operators)):
        if res is None:
            res = OPS[operators[i]](operands[i], operands[i + 1])
        else:
            res = OPS[operators[i]](res, operands[i + 1])
    return res


def is_valid(result:int, operands:list[int]):
    # if result < sum(operands) and 1 not in operands:
    #     return False
    # if result > mul(*operands) and 0 not in operands:
    #     return False
    start = operands[0]
    next_options = [(start, "*", 1), (start, "+", 1), (start, "|", 1)]
    while next_options:
        cur, op, idx = next_options.pop()
        res = OPS[op](cur,operands[idx])
        if res > result:
            continue
        if idx == len(operands) - 1 and res == result:
            return True
        if idx < len(operands) - 1:
            next_options += [(res, "*", idx+1), (res, "+", idx+1), (res, "|", idx+1)]
    return False


def main(example=False):
    res = 0
    for line in read_file(example):
        result, line = line.split(": ")
        operands = int_line(line, " ")
        if is_valid(int(result), operands):
            res += int(result)
    print(res)
    return res


assert main(True) == 11387
main()
