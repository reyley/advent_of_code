from utils.utils import read_file


class Monkey:
    diviser_list = []

    def __init__(self, lines):
        self.items = []
        self.op = None
        self.test = None
        self.parse(lines)
        self.num_inspected_items = 0

    def parse(self, lines):
        self.items = [int(_) for _ in lines[1].split(": ")[-1].split(", ")]
        op = lines[2].split("new = ")[-1]
        in_var_1, in_op, in_var_2 = op.split(" ")

        def op(old):
            var_1 = old if in_var_1 == "old" else int(in_var_1)
            var_2 = old if in_var_2 == "old" else int(in_var_2)
            if in_op == "+":
                return var_1 + var_2
            if in_op == "*":
                return var_1 * var_2
        self.op = op
        print("op 3: ", self.op(3))

        test_diviser = int(lines[3].split("divisible by ")[-1])
        test_true = int(lines[4].split("to monkey ")[-1])
        test_false = int(lines[5].split("to monkey ")[-1])
        self.test = lambda x: test_true if x % test_diviser == 0 else test_false
        print("test 1: ", self.test(1), f"test {test_diviser}: ", self.test(test_diviser))

    def inspect(self):
        if not self.items:
            return
        new = self.op(self.items[0]) // 3
        monkey = self.test(new)
        self.num_inspected_items += 1
        self.items.pop(0)
        return monkey, new

    def __repr__(self):
        return f"Items: {self.items}. n: {self.num_inspected_items}"


def play_game(monkeys, n_rounds):
    for r in range(n_rounds):
        for monkey in monkeys:
            while True:
                res = monkey.inspect()
                if not res:
                    break
                monkeys[res[0]].items.append(res[1])
        print(monkeys)


def get_res(monkeys):
    vals = [m.num_inspected_items for m in monkeys]
    vals.sort()
    res = vals[-1] * vals[-2]
    print(vals)
    return res


def main(example=False):
    monkeys = []
    monkey_lines = []
    for line in read_file(example):
        if not line and monkey_lines:
            monkeys.append(Monkey(monkey_lines))
            monkey_lines = []
        else:
            monkey_lines.append(line)
    monkeys.append(Monkey(monkey_lines))
    play_game(monkeys, 20)
    print(monkeys)
    return get_res(monkeys)


assert main(True) == 10605
print(main())
