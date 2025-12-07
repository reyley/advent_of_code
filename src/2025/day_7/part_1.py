from utils.utils import *


def main(example=False):
    grid = read_grid(example, start_ch="S")
    num_split = 0
    beams = {grid.start}
    for i in range(grid.n_rows):
        next_beams = set()
        for beam in beams:
            next_pos = go_down(beam)
            if grid.get(next_pos) == "^":
                num_split += 1
                next_beams.add(go_left(next_pos))
                next_beams.add(go_right(next_pos))
            else:
                next_beams.add(next_pos)
        beams = next_beams
    res = num_split
    print(res)
    return res


assert main(True) == 21
main()