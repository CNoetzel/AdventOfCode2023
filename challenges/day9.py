from itertools import pairwise
from typing import List


def extrapolate(input: List[int], next: bool) -> int:
    if all(val == 0 for val in input):
        return 0
    if next:
        return input[-1] + extrapolate([b - a for a, b in pairwise(input)], next)
    else:
        return input[0] - extrapolate([b - a for a, b in pairwise(input)], next)


def sum_sequence_values(data: List[str], next: bool) -> List[int]:
    return sum(
        [extrapolate(list(map(int, input.strip().split())), next) for input in data]
    )


def main():
    f = open("challenges/day9_input.txt", "r")
    lines = f.readlines()

    print(f"Task 1: The sum of next values is {sum_sequence_values(lines, True)}")
    print(f"Task 2: The sum of prev values is {sum_sequence_values(lines, False)}")


if __name__ == "__main__":
    main()
