import re
import utils

def part1_solution() -> int:
    input = utils.read_input(1)
    sum = 0
    for line in input.splitlines():
        digits = re.findall(r"[0-9]", line)
        sum += int(digits[0] + digits[-1])
    return sum
