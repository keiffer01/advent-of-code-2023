import utils

# key: color of cube, value: number of cubes
Round = dict[str, int]
Game = list[Round]
# key: Game ID, value: Game
Games = dict[int, Game]

def _clean_input(input: str ) -> Games:
    games = {}
    for line in input.splitlines():
        game_and_rounds = line.split(": ")
        game_id = int(game_and_rounds[0].split(" ")[1])
        game = []
        for round in game_and_rounds[1].split("; "):
            round_draws = list(
                map(lambda x: tuple(x.split(" ")), round.split(", "))
            )
            round_dict = {color: int(num) for (num, color) in round_draws}
            game.append(round_dict)
        games[game_id] = game
    return games

def _is_valid_cube_count(color: str, num: int) -> bool:
    if (color == "red" and num > 12 or
        color == "green" and num > 13 or
        color == "blue" and num > 14):
        return False
    return True

def part1_solution():
    games = _clean_input(utils.read_input(day=2))
    sum = 0
    for id, game in games.items():
        valid_game = True
        for round in game:
            for color, num in round.items():
                if not _is_valid_cube_count(color, num):
                    valid_game = False
                    break
            if not valid_game:
                break
        if valid_game:
            sum += id
    return sum

def part2_solution():
    games = _clean_input(utils.read_input(day=2))
    sum = 0
    for _, game in games.items():
        red = 0
        green = 0
        blue = 0
        for round in game:
            for color, num in round.items():
                if color == "red" and num > red:
                    red = num
                elif color == "green" and num > green:
                    green = num
                elif color == "blue" and num > blue:
                    blue = num
        print(red, green, blue)
        sum += red * green * blue
    return sum
