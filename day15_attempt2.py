# day 15 take 2
from typing import List

class NumberGame:
    def __init__(self, starting_numbers: List):
        self.numbers_in_game = {} # {turn_when_added: number}
        for i in range(len(starting_numbers)):
            self.numbers[i+1] = starting_numbers[i]
        self.turn = i + 2
        self.
    def get_nth_number(self, n):
        most_recent_turn = max(self.numbers_in_game.keys())
        most_recent_number = self.numbers_in_game[most_recent_turn]
        