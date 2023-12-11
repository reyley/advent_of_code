from utils.utils import read_file


class Board:
    def __init__(self, board):
        self.b = []
        self.marks = set()
        for line in board:
            self.b.append([int(x) for x in line.split(" ") if x])
        self.size = len(self.b)

    def get(self, i, j):
        return self.b[i][j]

    def check(self, i, j):
        j_s = {(k, j) for k in range(self.size)}
        if j_s.issubset(self.marks):
            return True
        i_s = {(i, k) for k in range(self.size)}
        if i_s.issubset(self.marks):
            return True
        return False

    def mark(self, num):
        for i in range(len(self.b)):
            for j in range(len(self.b[i])):
                if self.get(i, j) == num:
                    self.marks.add((i, j))
                    return self.check(i,j)
        return False

    def unmarked(self):
        s = 0
        for i in range(len(self.b)):
            for j in range(len(self.b[i])):
                if (i, j) not in self.marks:
                    s += self.get(i,j)
        return s


def parse_numbers(line):
    return [int(x) for x in line.split(",")]


def play_bingo(numbers, boards):
    for i, number in enumerate(numbers):
        for board in boards:
            if board.mark(number):
                return number * board.unmarked()
    return 0


def main(example=False):
    numbers = None
    board = []
    boards = []
    for i, line in enumerate(read_file(example)):
        if i == 0:
            numbers = parse_numbers(line)
            print(numbers)
        elif line:
            board.append(line)
        elif board:
            boards.append(Board(board))
            board = []
    boards.append(Board(board))
    res = play_bingo(numbers, boards)
    print(res)
    return res


assert main(True) == 4512
main()
