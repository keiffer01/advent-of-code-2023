import utils

def part1_solution():
    cards: list[str] = utils.read_input(day=4).splitlines()
    sum = 0
    for card in cards:
        sets = card.replace("  ", " ").split(": ")[1].split(" | ")
        winning_nums = {int(num) for num in sets[0].split(" ")}
        my_nums = {int(num) for num in sets[1].split(" ")}
        power = len(winning_nums & my_nums)
        if power > 0:
            sum += 2 ** (power - 1)
    return sum
