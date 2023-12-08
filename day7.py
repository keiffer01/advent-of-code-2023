import collections
import enum
import functools
import utils

CARD_STRENGTH_MAP = {
    "2": 0,
    "3": 1,
    "4": 2,
    "5": 3,
    "6": 4,
    "7": 5,
    "8": 6,
    "9": 7,
    "T": 8,
    "J": -1,
    "Q": 10,
    "K": 11,
    "A": 12
}

@functools.total_ordering
class HandType(enum.Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7

    def __lt__(self, other):
        if self.__class__ == other.__class__:
            return self.value < other.value
        return NotImplemented


@functools.total_ordering
class Hand:
    def __init__(self, line: str):
        spl = line.split(" ")
        self.cards = spl[0]
        self.bid = int(spl[1])

    def get_hand_type(self) -> HandType:
        card_counts = collections.Counter(self.cards)
        if "J" in card_counts and card_counts["J"] < 5:
            j_count = card_counts["J"]
            del card_counts["J"]
            highest_card = max(card_counts, key=card_counts.get)
            card_counts[highest_card] += j_count
        if len(card_counts.keys()) == 1:
            return HandType.FIVE_OF_A_KIND
        elif (len(card_counts.keys()) == 2 and
              set(card_counts.values()) == {4, 1}):
            return HandType.FOUR_OF_A_KIND
        elif (len(card_counts.keys()) == 2 and
              set(card_counts.values()) == {3, 2}):
            return HandType.FULL_HOUSE
        elif (len(card_counts.keys()) == 3 and
              set(card_counts.values()) == {3, 1, 1}):
            return HandType.THREE_OF_A_KIND
        elif (len(card_counts.keys()) == 3 and
              set(card_counts.values()) == {2, 2, 1}):
            return HandType.TWO_PAIR
        elif len(card_counts.keys()) == 4:
            return HandType.ONE_PAIR
        else:
            return HandType.HIGH_CARD

    def __lt__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        self_type = self.get_hand_type()
        other_type = other.get_hand_type()
        if self_type != other_type:
            return self_type < other_type
        for self_card, other_card in zip(self.cards, other.cards):
            if CARD_STRENGTH_MAP[self_card] == CARD_STRENGTH_MAP[other_card]:
                continue
            return CARD_STRENGTH_MAP[self_card] < CARD_STRENGTH_MAP[other_card]
        return False

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        self.cards == other.cards


# Need to change CARD_STRENGTH_MAP for this to work properly.
def part1_solution():
    hands = [Hand(line) for line in utils.read_input(day=7).splitlines()]
    hands.sort()
    result = 0
    for i, hand in enumerate(hands):
        result += hand.bid * (i + 1)
    return result

def part2_solution():
    hands = [Hand(line) for line in utils.read_input(day=7).splitlines()]
    hands.sort()
    result = 0
    for i, hand in enumerate(hands):
        result += hand.bid * (i + 1)
    return result
