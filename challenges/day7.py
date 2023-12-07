from typing import List
from enum import Enum

cards_value = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]


class Type(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7


class Hand:
    def __init__(self, cards: str, bid: int):
        self.cards = cards
        self.bid = bid
        self.type = self.determine_type()

    def has_same_card_times(self, times: int) -> bool:
        return any(self.cards.count(card) == times for card in self.cards)

    def determine_type(self):
        individual_cards = len(set(self.cards))
        if individual_cards == 5:
            return Type.HIGH_CARD
        elif individual_cards == 4:
            return Type.ONE_PAIR
        elif individual_cards == 3:
            # THREE_OF_A_KIND or TWO_PAIR
            if self.has_same_card_times(3):
                return Type.THREE_OF_A_KIND
            return Type.TWO_PAIR
        elif individual_cards == 2:
            # FOUR_OF_A_KIND or FULL_HOUSE
            if self.has_same_card_times(4):
                return Type.FOUR_OF_A_KIND
            return Type.FULL_HOUSE
        else:
            return Type.FIVE_OF_A_KIND

    def __repr__(self):
        return f"Hand({self.cards}, {self.bid}, {self.type})"

    def __lt__(self, other):
        if self.type == other.type:
            for idx in range(5):
                if self.cards[idx] == other.cards[idx]:
                    continue
                return cards_value.index(self.cards[idx]) < cards_value.index(
                    other.cards[idx]
                )
            return False
        return self.type.value < other.type.value


def total_winnings(data: List[str]) -> int:
    hands = [Hand(line.split(" ")[0], int(line.split(" ")[1])) for line in data]
    hands.sort()
    return sum((idx + 1) * hand.bid for idx, hand in enumerate(hands))


def main():
    f = open("challenges/day7_input.txt", "r")
    lines = f.readlines()

    print(f"Task 1: The total winnings are {total_winnings(lines)}")
    # too high 251032781
    # too high 250691712
    # too high 250518356
    # print(f"Task 2: The product of ways to win is {ways_to_win_single_race(lines)}")


if __name__ == "__main__":
    main()
