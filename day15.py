# day 15
from typing import List

def find_prev_num(num: int, list_of_nums: List[int]) -> int:
    start = len(list_of_nums) - 2
    for i in range(start, -1, -1):
        if list_of_nums[i] == num:
            return i

def play_game(starting_numbers, play_until = 2020, silent = True):
    t = len(starting_numbers) + 1
    while len(starting_numbers) < play_until:
        this_num = starting_numbers[-1]
        if not silent:
            print(f"Turn {t}: ", end = '\t')
        if this_num not in set(starting_numbers[:-1]):
            starting_numbers.append(0)
            if not silent: 
                print(f"{this_num} hasn't been spoken before so the next number spoken is 0")
        else:
            diff = len(starting_numbers)-1 - find_prev_num(this_num, starting_numbers)
            if not silent: 
                print(f"{this_num} has been spoken before so the next number spoken is {len(starting_numbers)-1} - {find_prev_num(this_num, starting_numbers)} = {diff}")
            starting_numbers.append(diff)
        t+=1
    return starting_numbers[-1]
    
assert play_game([0,3,6]) == 436, "[0,3,6] should lead to 436"
assert play_game([1,3,2]) == 1, "[1,3,2] should lead to 1"
assert play_game([2,1,3]) == 10, "[2,1,3] should lead to 10"
assert play_game([1,2,3]) == 27, "[1,2,3] should lead to 27"
assert play_game([2,3,1]) == 78, "[2,3,1] should lead to 78"
assert play_game([3,2,1]) == 438, "[3,2,1] should lead to 438"
assert play_game([3,1,2]) == 1836, "[3,1,2] should lead to 1836"

print(f"The 2020th number is {play_game([9,6,0,10,18,2,1])}")

# now find the 30000000th number
# we're going to have to refactor this I thinK!