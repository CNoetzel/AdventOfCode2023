import re
from typing import List
from functools import reduce

dices = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def is_game_possible(game_data: str):
    rounds = re.split(';', game_data.strip())
    for round in rounds:
        draw = re.split(',', round.strip())
        for dice_data in draw:
            dice = re.split(' ', dice_data.strip())
            if (dices[dice[1]] < int(dice[0])):
                return False
    return True

def calculate_power_of_set(game_data: str):
    dice_set = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    rounds = re.split(';', game_data.strip())
    for round in rounds:
        draw = re.split(',', round.strip())
        for dice_data in draw:
            dice = re.split(' ', dice_data.strip())
            if(dice_set[dice[1]] < int(dice[0])):
                dice_set[dice[1]] = int(dice[0])
    return reduce((lambda x, y: x * y), dice_set.values())

def get_sum_of_possible_games(data: List[str]):
    sum = 0
    for line in data:
        splitted = re.split(':', line)
        sum += int(splitted[0].replace('Game ', '')) if is_game_possible(splitted[1]) else 0
    return sum  
        
def get_sum_of_power_of_sets(data: List[str]): 
    sum = 0
    for line in data:
        splitted = re.split(':', line)
        sum += calculate_power_of_set(splitted[1])
    return sum     

def main():
    f = open('challenges/day2_input.txt', 'r')
    lines = f.readlines()

    print(f'Task 1: The sum of IDs of possible games is {get_sum_of_possible_games(lines)}')
    print(f'Task 2: The sum of the power of sets is {get_sum_of_power_of_sets(lines)}')

if __name__ == '__main__':
    main()