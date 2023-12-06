import re
from typing import List


def win_possibilities(time: int, distance_to_beat: int) -> List[int]:
    return [h for h in range(time) if h * (time - h) > distance_to_beat]


def product_of_ways_to_win(data: List[str]) -> int:
    time_data = list(map(int, data[0].replace("Time:", "").strip().split()))
    distance_data = list(map(int, data[1].replace("Distance:", "").strip().split()))

    result = 1
    for game_idx in range(0, len(time_data)):
        result *= len(win_possibilities(time_data[game_idx], distance_data[game_idx]))
    return result


def product_of_ways_to_win_single_race(data: List[str]) -> int:
    time_data = int(re.sub(r"(Time:|\s)", "", data[0]))
    distance_data = int(re.sub(r"(Distance:|\s)", "", data[1]))
    return len(win_possibilities(time_data, distance_data))


def main():
    f = open("challenges/day6_input.txt", "r")
    lines = f.readlines()

    print(f"Task 1: The product of ways to win is {product_of_ways_to_win(lines)}")
    print(
        f"Task 2: The product of ways to win is {product_of_ways_to_win_single_race(lines)}"
    )


if __name__ == "__main__":
    main()
