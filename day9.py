import utils

def _clean_input(input: str) -> list[list[int]]:
    lines = input.splitlines()
    return [[int(x) for x in line.split(" ")] for line in lines]

def part1_solution():
    histories = _clean_input(utils.read_input(day=9))
    extrapolations = []
    for history in histories:
        curr_history = history
        values = [history[-1]]
        while not all([x == 0 for x in curr_history]):
            new_history = []
            for first, second in zip(curr_history, curr_history[1:]):
                new_history.append(second - first)
            values.append(new_history[-1])
            curr_history = new_history
        while len(values) > 1:
            values.append(values.pop() + values.pop())
        extrapolations.append(values[0])
    return sum(extrapolations)

def part2_solution():
    histories = _clean_input(utils.read_input(day=9))
    extrapolations = []
    for history in histories:
        curr_history = history
        values = [history[0]]
        while not all([x == 0 for x in curr_history]):
            new_history = []
            for first, second in zip(curr_history, curr_history[1:]):
                new_history.append(second - first)
            values.append(new_history[0])
            curr_history = new_history
        while len(values) > 1:
            values.append(-values.pop() + values.pop())
        extrapolations.append(values[0])
    return sum(extrapolations)
