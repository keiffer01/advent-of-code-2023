import utils

# card should be in the format "Card _: 1 2 | 3 4 5".
def _count_winning_numbers(card: str) -> int:
    sets = card.replace("  ", " ").split(": ")[1].split(" | ")
    winning_nums = {int(num) for num in sets[0].split(" ")}
    my_nums = {int(num) for num in sets[1].split(" ")}
    return len(winning_nums & my_nums)


def part1_solution():
    cards: list[str] = utils.read_input(day=4).splitlines()
    sum = 0
    for card in cards:
        power = _count_winning_numbers(card)
        if power > 0:
            sum += 2 ** (power - 1)
    return sum

def part2_solution():
    cards: list[str] = utils.read_input(day=4).splitlines()
    card_counts = [1] * len(cards)
    for i, card in enumerate(cards):
        count = _count_winning_numbers(card)
        for j in range(min(len(cards), i + 1), min(len(cards), i + 1 + count)):
            card_counts[j] += card_counts[i]
    return sum(card_counts)
