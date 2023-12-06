from challenges import day6

test_input = ["Time:      7  15   30", "Distance:  9  40  200"]


def test_task1():
    result = day6.product_of_ways_to_win(test_input)
    assert result == 288


def test_task2():
    result = day6.product_of_ways_to_win_single_race(test_input)
    assert result == 71503
