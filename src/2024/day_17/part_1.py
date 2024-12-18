from utils.utils import *


class Opcode:
    ops = {}
    registers = {
        "A": 0,
        "B": 0,
        "C": 0
    }

    def __init__(self):
        for i in range(8):
            self.ops[i] = self.get_op(i)

    @classmethod
    def combo(cls, operand):
        if operand < 4:
            return operand
        if operand == 4:
            return cls.registers["A"]
        if operand == 5:
            return cls.registers["B"]
        if operand == 6:
            return cls.registers["C"]


    @classmethod
    def get_op(cls, opcode):
        match opcode:
            case 0:
                return cls.adv
            case 1:
                return cls.bxl
            case 2:
                return cls.bst
            case 3:
                return cls.jnz
            case 4:
                return cls.bxc
            case 5:
                return cls.out
            case 6:
                return cls.bdv
            case 7:
                return cls.cdv

    @classmethod
    def cdv(cls, operand):
        return cls.dv(operand, "C")

    @classmethod
    def bdv(cls, operand):
        return cls.dv(operand, "B")

    @classmethod
    def out(cls, operand):
        return {"output": cls.combo(operand) % 8}

    @classmethod
    def bxc(cls, operand):
        cls.registers["B"] = cls.registers["C"] ^ cls.registers["B"]
        return {}

    @classmethod
    def jnz(cls, operand):
        if cls.registers["A"]:
            return {"skip": operand}
        return {}

    @classmethod
    def bst(cls, operand):
        cls.registers["B"] = cls.combo(operand) % 8
        return {}

    @classmethod
    def bxl(cls, operand):
        res = operand ^ cls.registers["B"]
        cls.registers["B"] = res
        return {}

    @classmethod
    def adv(cls, operand):
        return cls.dv(operand, "A")

    @classmethod
    def dv(cls, operand, key):
        numerator = cls.registers["A"]
        denominator = 2**cls.combo(operand)
        res = numerator//denominator
        cls.registers[key] = res
        return {}


def run_program(program):
    i = 0
    output = []
    while i < len(program):
        assert i < len(program) - 1
        res = Opcode.ops[program[i]](program[i+1])
        if "output" in res:
            output.append(res["output"])
        if "skip" in res:
            i = res["skip"]
        else:
            i += 2
    return ",".join(str(x) for x in output)


def main(example=False):
    regex = re.compile("Register ([ABC]): (\d+)")
    Opcode()
    Opcode.registers = {
        "A": 0,
        "B": 0,
        "C": 0
    }
    program = []
    for line, part in read_split_file(example):
        if part == 1:
            for reg, num in regex.findall(line):
                Opcode.registers[reg] = int(num)
        if part == 2:
            line = line.replace("Program: ", "")
            program = int_line(line)
    res = run_program(program)
    print(res)
    return res


assert main(True) == "4,6,3,5,6,3,5,2,1,0"
main()
