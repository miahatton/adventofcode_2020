# day 15 take 2

from typing import List

class NumberGame:
    def __init__(self, starting_numbers: List):
        self.starting_numbers = starting_numbers
        self.numbers_in_game = {} # {number: (last_turn, turn before)}
        for i in range(len(starting_numbers)):
            self.numbers_in_game[starting_numbers[i]] = (i + 1, None)
        self.turn = i + 2
        self.last_number = starting_numbers[-1]
        print(f"New number game!\tStarting numbers: {self.numbers_in_game}")
    def reset(self):
        self.__init__(self.starting_numbers)
    def get_nth_number(self, n: int) -> int:
        print("Playing Number Game")
        while self.turn <= n:
            # consider the most recently spoken number (self.last_number)
            if self.numbers_in_game[self.last_number][1]:
                # It has been said before. The player finds the difference between this and the previous turn
                current_number = self.numbers_in_game[self.last_number][0] - self.numbers_in_game[self.last_number][1]
            else:
                # It has been not said before. The next number is 0
                current_number = 0
            # now record the answer 
            if current_number not in self.numbers_in_game.keys():
                # This number is new. Add to dictionary this number: (turn number, None)
                self.numbers_in_game[current_number] = (self.turn, None)
            else:
                 # This number is not new. Update dictionary this number: (turn number, previous turn number)
                self.numbers_in_game[current_number] = (self.turn, self.numbers_in_game[current_number][0])
            # add one to turn
            self.turn += 1
            self.last_number = current_number
        print(".....\nCompleted number game!")
        return self.last_number
 
def run_tests():
    test_starting_numbers = [[0,3,6], [1,3,2], [2,1,3], [1,2,3], [2,3,1], [3,2,1], [3,1,2]]         
    results = [436,1,10,27,78,438,1836]
    assert len(test_starting_numbers) == len(results), "List lengths do not match"
    for i in range(len(test_starting_numbers)):
        test_number_game = NumberGame(test_starting_numbers[i])
        assert test_number_game.get_nth_number(2020) == results[i], f"Starting numbers {starting_numbers[i]} should lead to {result[i]}"
    print("All tests passed")

run_tests()

starting_numbers = [9,6,0,10,18,2,1]

# part_one
print("Part one")
number_game = NumberGame(starting_numbers)
print(number_game.get_nth_number(2020))

# part_two
print("Part two")
print(number_game.get_nth_number(30000000))