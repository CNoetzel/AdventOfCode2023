import re
from typing import List
from functools import reduce


def get_seeds(seed_data: str) -> List[int]:
    sanitized = re.sub("seeds: ", "", seed_data.strip())
    return list(map(int, sanitized.strip().split()))


def build_mapping(data: List[str]):
    mapping = {}
    map_name = ""
    for idx in range(2, len(data)):
        line = data[idx].strip()
        if len(line) == 0:
            continue
        elif re.search(r"map:", line):
            map_name = re.sub(" map:", "", line)
            mapping[map_name] = []
        else:
            mapping[map_name].append(list(map(int, line.split())))
    return mapping


def get_mapping_value(input: int, map: List[List[int]]) -> int:
    for idx in range(len(map)):
        if input >= map[idx][1] and input <= map[idx][1] + map[idx][2] - 1:
            return map[idx][0] + (input - map[idx][1])
    return input


def get_nearest_location(data: List[str], seed_as_range: bool) -> int:
    seeds = get_seeds(data[0])
    mapping = build_mapping(data)

    location = None
    if seed_as_range:
        for idx in range(0, len(seeds), 2):
            for seed in range(seeds[idx], seeds[idx] + seeds[idx + 1]):
                out = seed
                for map in range(len(mapping)):
                    out = get_mapping_value(out, list(mapping.values())[map])
                location = out if location == None or out < location else location
    else:
        for seed in seeds:
            out = seed
            for map in range(len(mapping)):
                out = get_mapping_value(out, list(mapping.values())[map])
            location = out if location == None or out < location else location

    return location


def main():
    f = open("challenges/day5_input.txt", "r")
    lines = f.readlines()

    print(f"Task 1: The nearest location is {get_nearest_location(lines, False)}")
    # print(f"Task 2: The nearest location is {get_nearest_location(lines, True)}")


if __name__ == "__main__":
    main()
