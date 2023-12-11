from utils.utils import read_file

maxes = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def is_game_possible(game):
    for roll in game:
        number, color = roll.split(" ")
        number = int(number)
        if number > maxes.get(color, 0):
            return False
    return True

def main(example=False):
    res = 0
    for line in read_file(example):
        game_number, games = line.split(": ")
        game_number = int(game_number.strip("Game "))
        games = games.split("; ")
        if all(is_game_possible(game.split(", ")) for game in games):
            res += game_number


    print(res)
    return res


assert main(True) == 8
main()
