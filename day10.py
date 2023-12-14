import utils

class InvalidPathError(Exception):
    pass

def _clean_input(input: str) -> list[list[str]]:
    return [list(line) for line in input.splitlines()]

def find_S(map: list[list[str]]) -> tuple[int, int]:
    for i, row in enumerate(map):
        for j, tile in enumerate(row):
            if tile == "S":
                return (i, j)

def _get_next_tile_coords(map: list[list[str]],
                          curr_tile_coords: tuple[int, int],
                          prev_tile_coords: tuple[int, int], m: int,
                          n: int) -> tuple[int, int]:
    match map[curr_tile_coords[0]][curr_tile_coords[1]]:
        case "|":
            # Going south.
            if prev_tile_coords[0] == curr_tile_coords[0] - 1:
                if curr_tile_coords[0] == m - 1:
                    raise InvalidPathError
                else:
                    next_tile_coords = (curr_tile_coords[0] + 1,
                                        curr_tile_coords[1])
                    next_tile = map[next_tile_coords[0]][next_tile_coords[1]]
                    if (next_tile == "|" or next_tile == "L" or
                        next_tile == "J" or next_tile == "S"):
                        return next_tile_coords
                    raise InvalidPathError
            # Going nouth.
            else:
                if curr_tile_coords[0] == 0:
                    raise InvalidPathError
                else:
                    next_tile_coords = (curr_tile_coords[0] - 1,
                                        curr_tile_coords[1])
                    next_tile = map[next_tile_coords[0]][next_tile_coords[1]]
                    if (next_tile == "|" or next_tile == "7" or
                        next_tile == "F" or next_tile == "S"):
                        return next_tile_coords
                    raise InvalidPathError
        case "-":
            # Going east.
            if prev_tile_coords[1] == curr_tile_coords[1] - 1:
                if curr_tile_coords[1] == n - 1:
                    raise InvalidPathError
                else:
                    next_tile_coords = (curr_tile_coords[0],
                                        curr_tile_coords[1] + 1)
                    next_tile = map[next_tile_coords[0]][next_tile_coords[1]]
                    if (next_tile == "-" or next_tile == "J" or
                        next_tile == "7" or next_tile == "S"):
                        return next_tile_coords
                    raise InvalidPathError
            # Going west.
            else:
                if curr_tile_coords[1] == 0:
                    raise InvalidPathError
                else:
                    next_tile_coords = (curr_tile_coords[0],
                                        curr_tile_coords[1] - 1)
                    next_tile = map[next_tile_coords[0]][next_tile_coords[1]]
                    if (next_tile == "-" or next_tile == "L" or
                        next_tile == "F" or next_tile == "S"):
                        return next_tile_coords
                    raise InvalidPathError
        case "L":
            # Going east.
            if prev_tile_coords[0] == curr_tile_coords[0] - 1:
                if curr_tile_coords[1] == n - 1:
                    raise InvalidPathError
                else:
                    next_tile_coords = (curr_tile_coords[0],
                                        curr_tile_coords[1] + 1)
                    next_tile = map[next_tile_coords[0]][next_tile_coords[1]]
                    if (next_tile == "-" or next_tile == "J" or
                        next_tile == "7" or next_tile == "S"):
                        return next_tile_coords
                    raise InvalidPathError
            # Going north.
            else:
                if curr_tile_coords[0] == 0:
                    raise InvalidPathError
                else:
                    next_tile_coords = (curr_tile_coords[0] - 1,
                                        curr_tile_coords[1])
                    next_tile = map[next_tile_coords[0]][next_tile_coords[1]]
                    if (next_tile == "|" or next_tile == "7" or
                        next_tile == "F" or next_tile == "S"):
                        return next_tile_coords
                    raise InvalidPathError
        case "J":
            # Going west.
            if prev_tile_coords[0] == curr_tile_coords[0] - 1:
                if curr_tile_coords[1] == 0:
                    raise InvalidPathError
                else:
                    next_tile_coords = (curr_tile_coords[0],
                                        curr_tile_coords[1] - 1)
                    next_tile = map[next_tile_coords[0]][next_tile_coords[1]]
                    if (next_tile == "-" or next_tile == "L" or
                        next_tile == "F" or next_tile == "S"):
                        return next_tile_coords
                    raise InvalidPathError
            # Going north.
            else:
                if curr_tile_coords[0] == 0:
                    raise InvalidPathError
                else:
                    next_tile_coords = (curr_tile_coords[0] - 1,
                                        curr_tile_coords[1])
                    next_tile = map[next_tile_coords[0]][next_tile_coords[1]]
                    if (next_tile == "|" or next_tile == "7" or
                        next_tile == "F" or next_tile == "S"):
                        return next_tile_coords
                    raise InvalidPathError
        case "F":
            # Going east.
            if prev_tile_coords[0] == curr_tile_coords[0] + 1:
                if curr_tile_coords[1] == n - 1:
                    raise InvalidPathError
                else:
                    next_tile_coords = (curr_tile_coords[0],
                                        curr_tile_coords[1] + 1)
                    next_tile = map[next_tile_coords[0]][next_tile_coords[1]]
                    if (next_tile == "-" or next_tile == "J" or
                        next_tile == "7" or next_tile == "S"):
                        return next_tile_coords
                    raise InvalidPathError
            # Going south:
            else:
                if curr_tile_coords[0] == m - 1:
                    raise InvalidPathError
                else:
                    next_tile_coords = (curr_tile_coords[0] + 1,
                                        curr_tile_coords[1])
                    next_tile = map[next_tile_coords[0]][next_tile_coords[1]]
                    if (next_tile == "|" or next_tile == "L" or
                        next_tile == "J" or next_tile == "S"):
                        return next_tile_coords
                    raise InvalidPathError
        case "7":
            # Going west:
            if prev_tile_coords[0] == curr_tile_coords[0] + 1:
                if curr_tile_coords[1] == 0:
                    raise InvalidPathError
                else:
                    next_tile_coords = (curr_tile_coords[0],
                                        curr_tile_coords[1] - 1)
                    next_tile = map[next_tile_coords[0]][next_tile_coords[1]]
                    if (next_tile == "-" or next_tile == "L" or
                        next_tile == "F" or next_tile == "S"):
                        return next_tile_coords
                    raise InvalidPathError
            # Going south.
            else:
                if curr_tile_coords[0] == m - 1:
                    raise InvalidPathError
                else:
                    next_tile_coords = (curr_tile_coords[0] + 1,
                                        curr_tile_coords[1])
                    next_tile = map[next_tile_coords[0]][next_tile_coords[1]]
                    if (next_tile == "|" or next_tile == "L" or
                        next_tile == "J" or next_tile == "S"):
                        return next_tile_coords
                    raise InvalidPathError
        case _:
            raise InvalidPathError

def _count_path_to_S(map: list[list[str]], curr_tile_coords: tuple[int, int],
                     prev_tile_coords: tuple[int, int], m: int, n: int) -> int:
    count = 1
    while (map[curr_tile_coords[0]][curr_tile_coords[1]] != "S"):
        next_tile_coords = _get_next_tile_coords(map, curr_tile_coords,
                                                      prev_tile_coords, m, n)
        prev_tile_coords = curr_tile_coords
        curr_tile_coords = next_tile_coords
        count += 1
    return count

def part1_solution():
    map = _clean_input(utils.read_input(day=10))
    m = len(map)
    n = len(map[0])
    S_coords = find_S(map)
    potential_coords = [
        (S_coords[0] + 1, S_coords[1]),
        (S_coords[0] - 1, S_coords[1]),
        (S_coords[0], S_coords[1] + 1),
        (S_coords[0], S_coords[1] - 1),
    ]
    for coords in potential_coords:
        try:
            return _count_path_to_S(map, coords, S_coords, m, n) // 2
        except InvalidPathError:
            continue
