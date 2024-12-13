from utils.utils import *
from sympy import solve, Eq, Integer
from sympy.abc import a,b
import re

class Dot:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

class Machine:
    def __init__(self, A, B, P):
        self.a: Dot = A
        self.b: Dot = B
        self.p: Dot = P

    def solve(self):
        return solve([ Eq(self.a.x*a + self.b.x*b, self.p.x),
              Eq(self.a.y*a + self.b.y*b, self.p.y)])


re_button = re.compile("Button ([AB]): X\+(\d+), Y\+(\d+)")
re_p = re.compile("Prize: X=(\d+), Y=(\d+)")


def main(example=False):
    a_dot = b_dot = p_dot = None
    machines = []
    for line in read_file(example):
        if not line:
            machines.append(Machine(a_dot, b_dot, p_dot))
            a_dot = b_dot = p_dot = None
        elif line.startswith("Button"):
            matches = re_button.findall(line)
            for button, x,y in matches:
                if button == "A":
                    a_dot = Dot(x,y)
                else:
                    b_dot = Dot(x, y)
        else:
            matches = re_p.findall(line)
            for x,y in matches:
                p_dot = Dot(x,y)
    res = 0
    for m in machines:
        r = m.solve()
        r_a = r.get(a)
        r_b = r.get(b)
        if isinstance(r_a, Integer) and isinstance(r_b, Integer) and r_a >= 0 and r_b >= 0:
            res += 3*r_a + r_b
    print(res)
    return res


assert main(True) == 480
main()