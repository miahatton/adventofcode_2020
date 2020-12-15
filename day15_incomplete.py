# day 15
from typing import List

def play_game(starting_numbers: List[int], play_until = 2020, silent = True) -> int:
    indexes = [i + 1 for i in range(len(starting_numbers))]
    t = len(starting_numbers) + 1
    while t <= play_until:  # maybe should be <
        if not silent:
            print(f"Turn {t}: ")
        this_num = starting_numbers[-1]
        if this_num not in set(starting_numbers[:-1]):
            starting_numbers.append(0)
            if not silent: 
                print(f"{this_num} hasn't been spoken before so the next number spoken is 0")
        else:
            prev_num_pos = starting_numbers.index(this_num)
            prev_num_index = indexes[prev_num_pos]
            diff = indexes[-1] - prev_num_index
            if not silent: 
                print(f"{this_num} has been spoken before so the next number spoken is {indexes[-1]} - {prev_num_index} = {diff}")
            starting_numbers.append(diff)
            starting_numbers.pop(prev_num_pos)
            indexes.pop(prev_num_pos)
        indexes.append(t)
        if t%100000 == 0:
            print(f"Reached turn {t}")
        t+=1
    return starting_numbers[-1]
 
def run_tests():
    print("*"*20, "\tRunning tests\t", "*"*20)
    assert play_game([0,3,6], play_until = 10, silent = False) == 0, "[0,3,6] should lead to 0 after 10 turns"
    print("Test one complete")
    assert play_game([0,3,6]) == 436, "[0,3,6] should lead to 436"
    print("Test two complete")
    assert play_game([1,3,2]) == 1, "[1,3,2] should lead to 1"
    print("Test three complete")
    assert play_game([2,1,3]) == 10, "[2,1,3] should lead to 10"
    print("Test four complete")
    assert play_game([1,2,3]) == 27, "[1,2,3] should lead to 27"
    print("Test five complete")
    assert play_game([2,3,1]) == 78, "[2,3,1] should lead to 78"
    print("Test six complete")
    assert play_game([3,2,1]) == 438, "[3,2,1] should lead to 438"
    print("Test seven complete")
    assert play_game([3,1,2]) == 1836, "[3,1,2] should lead to 1836"
    print("*"*20, "\tTests complete\t", "*"*20)

run_tests()
print("\n","*"*20,"\tPart one\t", "*"*20)
print(f"The 2020th number is {play_game([9,6,0,10,18,2,1])}")

# now find the 30000000th number
# we're going to have to refactor this I thinK!

print("\n","*"*20,"\tPart two\t", "*"*20)
print("Test:", end = "\t")
print(f"The 30000000th number is {play_game([0,3,6], play_until = 30000000)}")
#print(f"The 30000000th number is {play_game([9,6,0,10,18,2,1], play_until = 30000000)}")