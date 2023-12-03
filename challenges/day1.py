import re
from typing import List
from functools import reduce

def getCalibrationValue(input: str) -> int:
    numbers = re.sub(r'\D','', input)
    return int(numbers[0] + numbers[len(numbers)-1])

def getCalibrationValueAdvanced(input: str) -> int:
    sanitized = re.sub(r'one','o1e', input)
    sanitized = re.sub(r'two','t2o', sanitized)
    sanitized = re.sub(r'three','t3e', sanitized)
    sanitized = re.sub(r'four','4r', sanitized)
    sanitized = re.sub(r'five','5e', sanitized)
    sanitized = re.sub(r'six','6', sanitized)
    sanitized = re.sub(r'seven','7n', sanitized)
    sanitized = re.sub(r'eight','e8t', sanitized)
    sanitized = re.sub(r'nine','n9e', sanitized)
    return getCalibrationValue(sanitized)


def sumCalibrationValues(data: List[str], func):
    return reduce((lambda x,y: x+y),[func(input) for input in data])

def main():
    f = open('challenges/day1_input.txt', 'r')
    lines = f.readlines()

    print(f'Task 1: Sum of calibration values is {sumCalibrationValues(lines, getCalibrationValue)}')
    print(f'Task 2: Sum of calibration values is {sumCalibrationValues(lines, getCalibrationValueAdvanced)}')
    
if __name__ == '__main__':
    main()