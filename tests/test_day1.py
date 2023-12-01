from challenges import day1
from challenges.utils import Task

def test_task1():
    input_task_1 = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
    result = day1.sumCalibrationValues(input_task_1, Task.TASK_1)
    assert result == 142
    
def test_task2():
    input_task_2 = ["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"]
    result = day1.sumCalibrationValues(input_task_2, Task.TASK_2)
    assert result == 281
