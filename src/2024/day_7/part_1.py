from functools import cache
from typing import Callable

from utils.utils import *

OPS = {
    "*": int.__mul__,
    "+": int.__add__
}

@cache
def function_combinations(length) -> set[list[Callable]]:
    prev_res = {"*", "+"}
    for i in range(1, length):
        res = set()
        res.update(x + "*" for x in prev_res)
        res.update(x + "+" for x in prev_res)
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
    operator_combos = function_combinations(len(operands) - 1)
    for operators in operator_combos:
        res = run(operators, operands)
        if res == result:
            return True
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


assert main(True) == 3749
main()
