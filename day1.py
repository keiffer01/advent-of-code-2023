import re
import utils

_digit_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0'
}

def _rewrite_digit(digit: str) -> str:
    if digit.isdigit():
        return digit
    return _digit_dict[digit]

def part1_solution() -> int:
    input = utils.read_input(1)
    sum = 0
    for line in input.splitlines():
        digits = re.findall(r"[0-9]", line)
        sum += int(digits[0] + digits[-1])
    return sum

def part2_solution() -> int:
    input = utils.read_input(1)
    sum = 0
    for line in input.splitlines():
        digits = re.findall(r"(?=(zero|one|two|three|four|five|six|seven|eight|nine|[0-9]))", line)
        sum += int(_rewrite_digit(digits[0]) + _rewrite_digit(digits[-1]))
    return sum
