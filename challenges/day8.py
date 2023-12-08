from math import lcm
from typing import List


def create_map(data: List[str]) -> dict[str, tuple]:
    map = {}
    for line in data:
        splitted = line.strip().split(" = ")
        map[splitted[0]] = tuple(splitted[1][1 : len(splitted[1]) - 1].split(", "))
    return map


def solve(pos: str, instructions: str, map: dict[str, tuple]) -> int:
    step_count = 0
    while not pos.endswith("Z"):
        for cmd in instructions:
            pos = map[pos][0 if cmd == "L" else 1]
            step_count += 1
            if pos.endswith("Z"):
                break
    return step_count


def required_steps(data: List[str]) -> int:
    instructions = data[0].strip()
    map = create_map(data[2 : len(data)])
    return solve("AAA", instructions, map)


def required_steps_as_ghost(data: List[str]) -> int:
    instructions = data[0].strip()
    map = create_map(data[2 : len(data)])
    pos = [pos for pos in map.keys() if pos.endswith("A")]
    # solve every start position individually and calculate lowest common multiple
    return lcm(*[solve(p, instructions, map) for p in pos])


def main():
    f = open("challenges/day8_input.txt", "r")
    lines = f.readlines()

    print(f"Task 1: Number of required steps is {required_steps(lines)}")
    print(f"Task 2: Number of required steps is {required_steps_as_ghost(lines)}")


if __name__ == "__main__":
    main()
