from typing import List
import re


def find_start_pos(data: List[str]) -> tuple:
    for idx, line in enumerate(data):
        start = re.search(r"S", line)
        if start:
            return (idx, start.span()[0])


def is_valid_connection(src: str, dest: str, dir: str) -> bool:
    if dest == ".":
        return False
    elif src == "S":
        return True
    elif dir == "north":
        return not src in ["-", "7", "F"] and dest in ["|", "7", "F", "S"]
    elif dir == "south":
        return not src in ["-", "L", "J"] and dest in ["|", "L", "J", "S"]
    elif dir == "west":
        return not src in ["|", "L", "F"] and dest in ["-", "L", "F", "S"]
    elif dir == "east":
        return not src in ["|", "J", "7"] and dest in ["-", "J", "7", "S"]
    else:
        return False


def next_pos(pos: List[tuple], data: List[str]) -> List[tuple]:
    predecessor = pos[-2] if len(pos) > 1 else pos[0]
    current = pos[-1]
    src = data[current[0]][current[1]]

    if current[0] > 0:
        dest_pos = (current[0] - 1, current[1])
        if predecessor != dest_pos and is_valid_connection(
            src, data[dest_pos[0]][dest_pos[1]], "north"
        ):
            return dest_pos
    if current[0] < len(data) - 1:
        dest_pos = (current[0] + 1, current[1])
        if predecessor != dest_pos and is_valid_connection(
            src, data[dest_pos[0]][dest_pos[1]], "south"
        ):
            return dest_pos
    if current[1] > 0:
        dest_pos = (current[0], current[1] - 1)
        if predecessor != dest_pos and is_valid_connection(
            src, data[dest_pos[0]][dest_pos[1]], "west"
        ):
            return dest_pos
    if current[1] < len(data[0]) - 1:
        dest_pos = (current[0], current[1] + 1)
        if predecessor != dest_pos and is_valid_connection(
            src, data[dest_pos[0]][dest_pos[1]], "east"
        ):
            return dest_pos


def steps_to_farthest_position(data: List[str]):
    pos = [find_start_pos(data)]
    while len(pos) == 1 or pos[0] != pos[-1]:
        pos.append(next_pos(pos, data))

    return int(len(pos) / 2)


def main():
    f = open("challenges/day10_input.txt", "r")
    lines = f.readlines()

    print(
        f"Task 1: Number of steps to the farthest position is {steps_to_farthest_position(lines)}"
    )
    # print(f"Task 2: The sum of prev values is {sum_sequence_values(lines, False)}")


if __name__ == "__main__":
    main()
