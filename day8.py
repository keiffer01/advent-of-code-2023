import re
import utils

def _construct_graph(input: str) -> dict[str, str]:
    graph = {}
    for line in input.splitlines():
        spl = line.split(" = ")
        graph[spl[0]] = spl[1].strip("()").split(", ")
    return graph

def part1_solution():
    input = utils.read_input(day=8)
    directions = re.search(r".*", input).group(0)
    graph = _construct_graph(re.search(r"(?ms)(?<=\n\n).*", input).group(0))
    curr_node = "AAA"
    count = 0
    while True:
        if curr_node == "ZZZ":
            return count

        for direction in directions:
            if curr_node == "ZZZ":
                return count

            if direction == "L":
                curr_node = graph[curr_node][0]
            else:
                curr_node = graph[curr_node][1]
            count += 1
