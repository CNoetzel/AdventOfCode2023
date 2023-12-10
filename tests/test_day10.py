from challenges import day10

test_input = [
    "..F7.",
    ".FJ|.",
    "SJ.L7",
    "|F--J",
    "LJ...",
]


def test_task1():
    result = day10.steps_to_farthest_position(test_input)
    assert result == 8


# def test_task2():
#    result = day9.sum_sequence_values(test_input)
#    assert result == 2
