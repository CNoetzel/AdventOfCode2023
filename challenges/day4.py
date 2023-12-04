import re
from typing import List
from functools import reduce


def intersection(lst1: List[int], lst2: List[int]) -> List[int]:
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


def get_matches_of_card(card: str) -> int:
    card_data = re.split(r"\s\|\s", card.strip())
    winning_numbers = list(map(int, card_data[0].strip().split()))
    own_numbers = list(map(int, card_data[1].strip().split()))
    return len(intersection(winning_numbers, own_numbers))


def get_points_of_cards(data: List[str]) -> int:
    sum = 0
    for line in data:
        matches = get_matches_of_card(re.split(":", line)[1])
        sum += pow(2, matches - 1) if matches > 0 else 0
    return sum


def get_amount_of_scratchpads(data: List[str]) -> int:
    instances = [0] * len(data)
    for card in range(len(data)):
        matches = get_matches_of_card(re.split(":", data[card])[1])
        instances[card] += 1
        for x in range(1, matches + 1):
            if card + x < len(instances):
                instances[card + x] += instances[card]
    return sum(instances)


def main():
    f = open("challenges/day4_input.txt", "r")
    lines = f.readlines()

    print(f"Task 1: The worth in points of all cards is {get_points_of_cards(lines)}")
    print(f"Task 2: We end up with {get_amount_of_scratchpads(lines)} scratchpads")


if __name__ == "__main__":
    main()
