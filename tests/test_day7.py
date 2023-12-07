from challenges import day7

test_input = ["32T3K 765", "T55J5 684", "KK677 28", "KTJJT 220", "QQQJA 483"]


def test_task1():
    result = day7.total_winnings(test_input)
    assert result == 6440


# def test_task2():
#    result = day6.ways_to_win_single_race(test_input)
#    assert result == 71503
