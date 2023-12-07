from challenges import day7

test_input = ["32T3K 765", "T55J5 684", "KK677 28", "KTJJT 220", "QQQJA 483"]


def test_task1():
    result = day7.total_winnings(test_input, False)
    assert result == 6440


def test_task2():
    result = day7.total_winnings(test_input, True)
    assert result == 5905
