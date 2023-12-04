from challenges import day3

test_input = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598..",
]


def test_task1():
    result = day3.get_sum_of_part_numbers(test_input)
    assert result == 4361


def test_task2():
    result = day3.get_sum_of_all_gear_ratios(test_input)
    assert result == 467835
