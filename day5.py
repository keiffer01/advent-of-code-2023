import re
import utils

seeds_regex = r"(?ms)(?<=seeds: ).*(?=\nseed-to-soil)"
seed_soil_regex = r"(?ms)(?<=seed-to-soil map:\n).*(?=\nsoil-to-fertilizer)"
soil_fertilizer_regex = r"(?ms)(?<=soil-to-fertilizer map:\n).*(?=\nfertilizer-to-water)"
fertilizer_water_regex = r"(?ms)(?<=fertilizer-to-water map:\n).*(?=\nwater-to-light)"
water_light_regex = r"(?ms)(?<=water-to-light map:\n).*(?=\nlight-to-temperature)"
light_temperature_regex = r"(?ms)(?<=light-to-temperature map:\n).*(?=\ntemperature-to-humidity)"
temperature_humidity_regex = r"(?ms)(?<=temperature-to-humidity map:\n).*(?=\nhumidity-to-location)"
humidity_location_regex = r"(?ms)(?<=humidity-to-location map:\n).*"

def _generate_maps(input: str, regexes: list[str]) -> list[list[list[int]]]:
    result = []
    for regex in regexes:
        string_map = re.search(regex, input).group(0)
        result.append([[int(num) for num in line.split(" ")]
                       for line in string_map.splitlines()])
    return result

def _find_next_num(seed: int, map: list[list[int]]) -> int:
    for mapping in map:
        end = mapping[0]
        start = mapping[1]
        length = mapping[2]
        if start <= seed and seed < start + length:
            return seed - start + end
    return seed

def _walk_through_maps(seed :int , maps: list[list[list[int]]]) -> int:
    for map in maps:
        seed = _find_next_num(seed, map)
    return seed

def part1_solution():
    input = utils.read_input(day=5)
    all_maps = _generate_maps(input, [
        seed_soil_regex, soil_fertilizer_regex, fertilizer_water_regex,
        water_light_regex, light_temperature_regex, temperature_humidity_regex,
        humidity_location_regex
    ])
    seeds = [int(seed) for seed in
             re.search(seeds_regex, input).group(0).split(" ")]
    lowest_location = None
    for seed in seeds:
        location = _walk_through_maps(seed, all_maps)
        if lowest_location == None:
            lowest_location = location
        elif location < lowest_location:
            lowest_location = location
    return lowest_location
