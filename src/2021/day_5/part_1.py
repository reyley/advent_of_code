from utils.utils import read_file


def get_mid_values(val1, val2):
    direction = 1 if val2 > val1 else -1
    return list(range(val1, val2 + direction, direction))


def add_points(total_points, double_points, point1, point2):
    x1, y1 = map(int, point1.split(","))
    x2, y2 = map(int, point2.split(","))
    points = set()
    if x1 == x2:
        points = {(x1, y) for y in range(min(y1, y2), max(y1, y2) + 1)}
    elif y1 == y2:
        points = {(x, y1) for x in range(min(x1, x2), max(x1, x2) + 1)}
    double_points.update(points.intersection(total_points))
    total_points.update(points)


def main(example=False):
    total_points = set()
    double_points = set()
    for line in read_file(example):
        point1, point2 = line.split(" -> ")
        add_points(total_points, double_points, point1, point2)
        pass
    res = len(double_points)
    print(res)
    return res


assert main(True) == 5
main()
