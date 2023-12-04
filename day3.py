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

# Returns 0 if not a valid gear. Gear is located at (row, col).
def _get_gear_ratio(schematic: list[str], row: int, col: int) -> int:
    adjacent_nums = []
    for r in range(max(0, row - 1), min(len(schematic), row + 2)):
        for m in re.finditer(r"[0-9]+", schematic[r]):
            if ((m.start() >= col - 1 and m.start() <= col + 1) or
               (m.end() >= col and m.end() <= col + 2) or
               (m.start() < col - 1 and m.end() > col + 2)):
                adjacent_nums.append(m.group(0))
    if len(adjacent_nums) == 2:
        return int(adjacent_nums[0]) * int(adjacent_nums[1])
    return 0

def part1_solution():
    schematic = utils.read_input(day=3).splitlines()
    sum = 0
    for i, line in enumerate(schematic):
        for m in re.finditer(r"[0-9]+", line):
            if _is_valid_part_number(schematic, i, m):
                sum += int(m.group(0))
    return sum

def part2_solution():
    schematic = utils.read_input(day=3).splitlines()
    sum = 0
    for i, line in enumerate(schematic):
        for m in re.finditer(r"\*", line):
            sum += _get_gear_ratio(schematic, i, m.start())
    return sum
