from utils.utils import read_file


def step(x, y, v_x, v_y):
    x, y = x + v_x, y + v_y
    v_x = 0 if v_x == 0 else v_x - 1 if v_x > 0 else v_x + 1
    v_y -= 1
    # print("step ", x, y, v_x, v_y)
    return x, y, v_x, v_y

def extract_range(r: str):
    r = r[2:]
    start, end = r.split("..")
    return int(start), int(end)

def find_x_v_start(x_range):
    x = 0
    n = 1
    start = 0
    end = 0
    while x <= x_range[1]:
        if x + n >= x_range[0] and not start:
            start = n
        if x + n > x_range[1]:
            end = n
            break
        x += n
        n += 1
    return start, end

def get_height(v_x, v_y, x_range, y_range):
    print("attempt ", v_x, v_y, x_range, y_range)
    x, y = 0, 0
    max_h = 0
    while True:
        x, y, v_x, v_y = step(x, y, v_x, v_y)
        if y > max_h:
            max_h = y
        hit = x_range[0] <= x <= x_range[1] and y_range[0] <= y <= y_range[1]
        if hit:
            print(v_x, v_y, max_h)
            return max_h
        miss = x > x_range[1] or y < y_range[0]
        if miss:
            return None

def find_max_height(x_range, y_range):
    print(x_range, y_range)
    x_v_start, x_v_end = find_x_v_start(x_range)
    print(x_v_start, x_v_end)
    y_v_start = abs(y_range[0])
    max_height = 0
    for x_v in range(x_v_start, x_v_end):
        for y_v in range(y_v_start, 0, -1):
            h = get_height(x_v, y_v, x_range, y_range)
            if h is not None and h > max_height:
                max_height = h
            elif h is not None:
                break
    return max_height

def main(example=False):
    for line in read_file(example):
        line = line.replace("target area: ", "")
        x_str, y_str = line.split(", ")
        x_range = extract_range(x_str)
        y_range = extract_range(y_str)
    res = find_max_height(x_range, y_range)
    print(res)
    return res


assert main(True) == 45
main()
