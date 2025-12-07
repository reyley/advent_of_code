from utils.utils import *

def add_beam(beams, pos, count):
    if pos in beams:
        beams[pos] += count
    else:
        beams[pos] = count

def main(example=False):
    grid = read_grid(example, start_ch="S")
    num_timelines = 1
    beams = dict()
    beams[grid.start] = 1
    for i in range(grid.n_rows):
        next_beams = dict()
        for beam in beams:
            next_pos = go_down(beam)
            if grid.get(next_pos) == "^":
                num_timelines += beams[beam]
                add_beam(next_beams, go_left(next_pos), beams[beam])
                add_beam(next_beams, go_right(next_pos), beams[beam])
            else:
                add_beam(next_beams, next_pos, beams[beam])
        beams = next_beams
    res = num_timelines
    print(res)
    return res


assert main(True) == 40
main()