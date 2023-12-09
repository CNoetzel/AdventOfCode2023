from challenges import day9

test_input = [
    "0 3 6 9 12 15",
    "1 3 6 10 15 21",
    "10 13 16 21 30 45",
]


def test_task1():
    result = day9.sum_sequence_values(test_input, True)
    assert result == 114


def test_task2():
    result = day9.sum_sequence_values(test_input, False)
    assert result == 2
