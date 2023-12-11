from utils.utils import read_file


class Item:
    def __init__(self, diviser_list, number):
        self.mods = {x: number % x for x in diviser_list}

    def add(self, n):
        for x in self.mods:
            self.mods[x] = (self.mods[x] + n) % x

    def mul(self, n):
        for x in self.mods:
            self.mods[x] = (self.mods[x] * n) % x

    def sq(self):
        for x in self.mods:
            self.mods[x] = (self.mods[x] ** 2) % x

    def is_div(self, x):
        return self.mods[x] == 0

    def __repr__(self):
        return repr(self.mods)


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

        def op(old: Item):
            var_1 = old if in_var_1 == "old" else int(in_var_1)
            var_2 = old if in_var_2 == "old" else int(in_var_2)
            if var_1 == old and var_2  == old:
                return old.sq()
            if in_op == "+":
                return old.add(var_2)
            if in_op == "*":
                return old.mul(var_2)
        self.op = op
        # print("op 3: ", self.op(Item([3,5,7], 3)))

        test_diviser = int(lines[3].split("divisible by ")[-1])
        Monkey.diviser_list.append(test_diviser)
        test_true = int(lines[4].split("to monkey ")[-1])
        test_false = int(lines[5].split("to monkey ")[-1])
        self.test = lambda x: test_true if x.is_div(test_diviser) else test_false
        # print("test 1: ", self.test(Item([3,5,7], 3)), f"test {test_diviser}: ", self.test(Item([3,5,7], 3)))

    def convert_to_items(self):
        for i in range(len(self.items)):
            self.items[i] = Item(Monkey.diviser_list, self.items[i])
        print(self.items)

    def inspect(self):
        if not self.items:
            return
        item = self.items.pop(0)
        self.op(item)
        monkey = self.test(item)
        self.num_inspected_items += 1
        return monkey, item

    def __repr__(self):
        return f"Items: {self.items}. n: {self.num_inspected_items}"


def play_game(monkeys, n_rounds):
    for r in range(n_rounds):
        print(r)
        for monkey in monkeys:
            while True:
                res = monkey.inspect()
                if not res:
                    break
                monkeys[res[0]].items.append(res[1])

    Monkey.diviser_list = []
        # print(monkeys)


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
    for m in monkeys:
        m.convert_to_items()
    play_game(monkeys, 10000)
    # print(monkeys)
    return get_res(monkeys)


assert main(True) == 2713310158
print(main())
