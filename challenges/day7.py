from typing import List
from enum import Enum

# global flag for controlling if Js should be considered as jokers and card values
# for the two different cases
js_are_jokers = False
cards_value = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
cards_value_jokers = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]


class Type(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7


# Mapping of types if the hand contains jokers
# HIGH_CARD with one joker will become ONE_PAIR, ...
joker_mapping = {
    "HIGH_CARD": [
        Type.ONE_PAIR,
        Type.THREE_OF_A_KIND,
        Type.FOUR_OF_A_KIND,
        Type.FIVE_OF_A_KIND,
    ],
    "ONE_PAIR": [
        Type.THREE_OF_A_KIND,
        Type.FOUR_OF_A_KIND,
        Type.FIVE_OF_A_KIND,
    ],
    "TWO_PAIR": [
        Type.FULL_HOUSE,
    ],
    "THREE_OF_A_KIND": [
        Type.FOUR_OF_A_KIND,
        Type.FIVE_OF_A_KIND,
    ],
    "FULL_HOUSE": [Type.FULL_HOUSE],
    "FOUR_OF_A_KIND": [Type.FIVE_OF_A_KIND],
}


# Class containing the logic for determining type of hand
# and algorithm to sort hands
class Hand:
    def __init__(self, cards: str, bid: int):
        self.cards = cards
        self.bid = bid
        self.type = (
            self.determine_type_with_jokers()
            if js_are_jokers
            else self.determine_type(self.cards, 0)
        )

    def has_same_card_times(self, times: int) -> bool:
        return any(self.cards.count(card) == times for card in self.cards)

    def determine_type_with_jokers(self) -> Type:
        number_of_jokers = self.cards.count("J")
        if number_of_jokers == 0:
            return self.determine_type(self.cards, 0)
        elif number_of_jokers == 5:
            return Type.FIVE_OF_A_KIND
        sanitized_cards = self.cards.replace("J", "")
        base_type = self.determine_type(sanitized_cards, -number_of_jokers)
        return joker_mapping[base_type.name][number_of_jokers - 1]

    def determine_type(self, cards: str, offset: int) -> Type:
        individual_cards = len(set(cards))
        if individual_cards == 5 + offset:
            return Type.HIGH_CARD
        elif individual_cards == 4 + offset:
            return Type.ONE_PAIR
        elif individual_cards == 3 + offset:
            # THREE_OF_A_KIND or TWO_PAIR
            if self.has_same_card_times(3):
                return Type.THREE_OF_A_KIND
            return Type.TWO_PAIR
        elif individual_cards == 2 + offset:
            # FOUR_OF_A_KIND or FULL_HOUSE
            if self.has_same_card_times(4):
                return Type.FOUR_OF_A_KIND
            return Type.FULL_HOUSE
        else:
            return Type.FIVE_OF_A_KIND

    def __repr__(self):
        return f"Hand({self.cards}, {self.bid}, {self.type})"

    def __lt__(self, other):
        value_list = cards_value_jokers if js_are_jokers else cards_value
        if self.type == other.type:
            for idx in range(5):
                if self.cards[idx] == other.cards[idx]:
                    continue
                return value_list.index(self.cards[idx]) < value_list.index(
                    other.cards[idx]
                )
            return False
        return self.type.value < other.type.value


def total_winnings(data: List[str], jokers: bool) -> int:
    global js_are_jokers
    js_are_jokers = jokers
    hands = [Hand(line.split(" ")[0], int(line.split(" ")[1])) for line in data]
    hands.sort()
    return sum((idx + 1) * hand.bid for idx, hand in enumerate(hands))


def main():
    f = open("challenges/day7_input.txt", "r")
    lines = f.readlines()

    print(f"Task 1: The total winnings are {total_winnings(lines, False)}")
    print(f"Task 2: The total winnings are {total_winnings(lines, True)}")


if __name__ == "__main__":
    main()
