from utils.utils import read_file

def get_maxes(game, maxes):
    for roll in game:
        number, color = roll.split(" ")
        number = int(number)
        maxes[color] = max(number, maxes.get(color, 0))

def get_game_min_cubes_num(games):
    maxes = {}
    for game in games:
        get_maxes(game.split(", "), maxes)
    res = 1
    for x in maxes.values():
        res *= x
    return res

def main(example=False):
    res = 0
    for line in read_file(example):
        game_number, games = line.split(": ")
        game_number = int(game_number.strip("Game "))
        games = games.split("; ")
        res += get_game_min_cubes_num(games)


    print(res)
    return res


assert main(True) == 2286
main()
