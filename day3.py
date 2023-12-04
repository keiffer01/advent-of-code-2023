import re
import utils

def _is_valid_part_number(schematic: list[str], row: int,
                          m: re.Match[str]) -> bool:
    start = 0 if m.start() == 0 else m.start() - 1
    end = len(schematic[0]) if m.end() == len(schematic[0]) else m.end() + 1
    regex = r"(?!([0-9]|\.|$))"
    if row != 0 and re.search(regex, schematic[row - 1][start:end]) != None:
        return True
    if re.search(regex, schematic[row][start:end]) != None:
        return True
    if (row != len(schematic) - 1 and
        re.search(regex, schematic[row + 1][start:end]) != None):
        return True
    return False


def part1_solution():
    schematic = utils.read_input(day=3).splitlines()
    sum = 0
    for i, line in enumerate(schematic):
        for m in re.finditer(r"[0-9]+", line):
            if _is_valid_part_number(schematic, i, m):
                sum += int(m.group(0))
    return sum
