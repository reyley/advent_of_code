import random

from utils.utils import *

import numpy as np
from scipy.optimize import fsolve
import z3


class Hail:
    all = None

    def __init__(self, line):
        coord, v = line.split(" @ ")
        self.x,self.y,self.z = int_space_line(coord)
        self.v_x, self.v_y, self.v_z = int_space_line(v)
        Hail.all.append(self)

    def is_parallel(self, other):
        return self.v_x/other.v_x == self.v_y/other.v_y == self.v_z/other.v_z

    def intersection(self, other):
        if other.v_x*self.v_y == self.v_x*other.v_y: # parallel
            return None, None
        denom = other.v_x - (self.v_x*other.v_y)/self.v_y
        t_1 = (self.x - other.x + (self.v_x*other.y)/self.v_y - (self.v_x*self.y)/self.v_y)/denom
        t_0 = (other.y + other.v_y*t_1 - self.y)/self.v_y
        if t_0 < 0 or t_1 < 0:
            return None, None
        x = self.x + t_0*self.v_x
        y = self.y + t_0*self.v_y
        x1 = other.x + t_1*other.v_x
        y1 = other.y + t_1*other.v_y
        print(f"{x=}, {y=}   {x1=}, {y1=}")
        print(f"{t_1=}, {t_0=}")

        # assert abs(x - x1) < 0.1
        # assert abs(y - y1) < 0.1
        return x,y

    def __repr__(self):
        return f"{self.x},{self.y},{self.z} @ {self.v_x},{self.v_y},{self.v_z}"


def non_linear_eq(w, hail):
    # w[0:3] == x,y,z of solution
    # w[3:6] == v_x, v_y, v_z of solution
    # w[6:9] == t0, t1, t2 of solution - aka the time the solution hits the first 3 hailstones

    F = np.zeros(9)
    F[0] = hail[0].x + hail[0].v_x * w[6] - w[6] * w[3] - w[0]
    F[1] = hail[0].y + hail[0].v_y * w[6] - w[6] * w[4] - w[1]
    F[1] = hail[0].z + hail[0].v_z * w[6] - w[6] * w[5] - w[2]
    F[3] = hail[1].x + hail[1].v_x * w[7] - w[7] * w[3] - w[0]
    F[4] = hail[1].y + hail[1].v_y * w[7] - w[7] * w[4] - w[1]
    F[5] = hail[1].z + hail[1].v_z * w[7] - w[7] * w[5] - w[2]
    F[6] = hail[2].x + hail[2].v_x * w[8] - w[8] * w[3] - w[0]
    F[7] = hail[2].y + hail[2].v_y * w[8] - w[8] * w[4] - w[1]
    F[8] = hail[2].z + hail[2].v_z * w[8] - w[8] * w[5] - w[2]
    return F

def solve(hail):
    x,y,z,vx,vy,vz,t0,t1,t2 = z3.Ints('x y z vx vy vz t0 t1 t2')
    s = z3.Solver()
    s.add(t0 >= 0)
    s.add(t1 >= 0)
    s.add(t2 >= 0)
    s.add(x + vx * t0 == hail[0].x + hail[0].v_x * t0)
    s.add(y + vy * t0 == hail[0].y + hail[0].v_y * t0)
    s.add(z + vz * t0 == hail[0].z + hail[0].v_z * t0)
    s.add(x + vx * t1 == hail[1].x + hail[1].v_x * t1)
    s.add(y + vy * t1 == hail[1].y + hail[1].v_y * t1)
    s.add(z + vz * t1 == hail[1].z + hail[1].v_z * t1)
    s.add(x + vx * t2 == hail[2].x + hail[2].v_x * t2)
    s.add(y + vy * t2 == hail[2].y + hail[2].v_y * t2)
    s.add(z + vz * t2 == hail[2].z + hail[2].v_z * t2)
    s.check()
    m = s.model()
    print(m)
    return int(str(m[x])) + int(str(m[y]))+ int(str(m[z]))


def main(example=False):
    Hail.all = []
    for line in read_file(example):
        Hail(line)

    res = 0
    for i in range(len(Hail.all) - 3):
        hail = Hail.all[i:i+3]
        initial_guess = [random.randint(-1**10, 10**10) for i in range(9)]
        solution_info = fsolve(non_linear_eq, initial_guess, args=(hail,), full_output=1, maxfev=5000000, xtol=1.49012e-16)
        print(non_linear_eq(solution_info[0], hail))
        print(solution_info)
        if solution_info[2] == 1:
            # This means that it might be solvable with these hailstones
            print(solution_info[0])
            print(solution_info)
            # This actually solves the equation exactly
            res = solve(hail)
            break
    print(res)
    return res


assert main(True) == 47
main()
