import functools
import re
import utils

def part1_solution():
    input = re.sub(r" +", r" ", utils.read_input(day=6)).splitlines()
    times = [int(time) for time in input[0].split(": ")[1].split(" ")]
    distances = [int(distance) for distance in 
                 input[1].split(": ")[1].split(" ")]
    results = []
    for time, distance in zip(times, distances):
        count = 0
        for i in range(time + 1):
            if i * (time - i) > distance:
                count += 1
        results.append(count)
    return functools.reduce(lambda x, y: x * y, results, 1)

def part2_solution():
    input = re.sub(r" +", r"", utils.read_input(day=6)).splitlines()
    time = int(input[0].split(":")[1])
    distance = int(input[1].split(":")[1])
    count = 0
    for i in range(time + 1):
        if i * (time - i) > distance:
            count += 1
    return count
