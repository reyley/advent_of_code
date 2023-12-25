from utils.utils import *

class Hail:
    all = None
    def __init__(self, line):
        coord, v = line.split(" @ ")
        self.x,self.y,self.z = int_space_line(coord)
        self.v_x, self.v_y, self.v_z = int_space_line(v)
        Hail.all.append(self)

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

def main(example=False):
    Hail.all = []
    for line in read_file(example):
        Hail(line)
    res = 0
    min_, max_ = 200000000000000, 400000000000000
    for i, h1 in enumerate(Hail.all):
        for h2 in  Hail.all[i+1:]:
            x,y = h1.intersection(h2)
            if x is not None:
                if min_ <= x <= max_ and min_ <= y <= max_:
                    res += 1
    print(res)
    return res


assert main(True) == 0
main()
