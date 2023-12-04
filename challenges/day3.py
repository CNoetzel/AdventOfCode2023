import re
from typing import List
from functools import reduce


def is_adjacent(num_pos: tuple[int, int], symbol_pos: int) -> bool:
    return (
        (num_pos[0] <= symbol_pos and num_pos[1] > symbol_pos)
        or num_pos[1] == symbol_pos
        or num_pos[0] == symbol_pos + 1
    )


# collect adjacent numbers for a row
def get_adjacent_numbers(symbol_column_idx: int, row_to_check: str) -> List[int]:
    numbers = []
    for match in re.finditer(r"\d+", row_to_check):
        if is_adjacent(match.span(), symbol_column_idx):
            numbers.append(int(match.group(0)))
    return numbers


# collect adjacent numbers for each symbol
def process_symbol(row: int, column: int, data: List[str], func) -> int:
    adjacent_numbers = []
    # Check same row
    adjacent_numbers.extend(get_adjacent_numbers(column, data[row]))
    if row != 0:  # Check row above
        adjacent_numbers.extend(get_adjacent_numbers(column, data[row - 1]))
    if row != len(data) - 1:  # Check row below
        adjacent_numbers.extend(get_adjacent_numbers(column, data[row + 1]))
    return func(adjacent_numbers)


# find symbols in rows and process every match
def process_data(data: List[str], regex: re.Pattern[str], func):
    sum = 0
    for row in range(0, len(data)):
        for symbol_match in re.finditer(regex, data[row].strip()):
            column = symbol_match.span()[0]
            sum += process_symbol(row, column, data, func)
    return sum


def get_sum_of_adjacent_numbers(adjacent_numbers: List[int]) -> int:
    return (
        reduce((lambda x, y: x + y), adjacent_numbers)
        if len(adjacent_numbers) > 0
        else 0
    )


def get_product_of_adjacent_gears(adjacent_numbers: List[int]) -> int:
    return (
        reduce((lambda x, y: x * y), adjacent_numbers)
        if len(adjacent_numbers) == 2
        else 0
    )


def get_sum_of_part_numbers(data: List[str]) -> int:
    # Check for all symbols and pass function to add adjacent numbers
    return process_data(data, r"[^\.\d]", get_sum_of_adjacent_numbers)


def get_sum_of_all_gear_ratios(data: List[str]) -> int:
    # Check for '*' symbol and pass function to multiply numbers when there are exactly two adjacent numbers
    return process_data(data, r"\*", get_product_of_adjacent_gears)


def main():
    f = open("challenges/day3_input.txt", "r")
    lines = f.readlines()

    print(f"Task 1: The sum of part numbers is {get_sum_of_part_numbers(lines)}")
    print(
        f"Task 2: The sum of all of the gear ratios is {get_sum_of_all_gear_ratios(lines)}"
    )


if __name__ == "__main__":
    main()
