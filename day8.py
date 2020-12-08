from funcs import read_input
from typing import List

class Code:
    
    code = []       # list of instructions and steps
    temp_code = []  # duplicate of code that can be altered for testing
    
    def __init__(self, input_strings: List):
        self.input_strings = input_strings
        self.code = self.read_input_strings()
        self.reset()
        
    def read_input_strings(self) -> List[(str, int)]:
        """
        Split the input strings into tupes of instruction and step number
        """
        return [
                (ins, int(step)) for ins, step in 
                [line.split(' ') for line in self.input_strings]
                ]
        
    def reset(self):
        """
        Reset the program's index, accumulator, list of indexes run and temp code.
        """
        self.index = 0
        self.acc = 0
        self.index_run = []
        self.temp_code = self.read_input_strings()

    def append_index(self):
        """
        Add the currently selected index to list of indexes run
        """
        self.index_run.append(self.index)
        
    def accumulator(self, i: int, code_to_run: List(str, int)) -> int:
        """
        Perform 'acc' operation - increase accumulator by step number
        Append current index to list of indexes run
        """
        self.acc += code_to_run[i][1]
        self.append_index()
        return i + 1
    
    def jump(self, i: int, code_to_run):
        """
        Append current index to list of indexes run
        Perform 'jmp' operation - increase selected index by step number
        """
        self.append_index()
        return i + code_to_run[i][1]
    
    def nop(self, i: int):
        """
        Append current index to list of indexes run
        Perform 'nop' operation - increase index by 1
        """
        self.append_index
        return i + 1
    
    def test_code(self, code_to_run: List[str, int]):
        """
        Find the point at which an infinite loop begins by following 
        each instruction until an index is encountered that has already
        been used. 
        """
        while self.index not in self.index_run:
            # Keep running code until duplicate row is reached
            if code_to_run[self.index][0] == 'acc':
                self.index = self.accumulator(self.index, code_to_run)
            elif code_to_run[self.index][0] == 'jmp':
                self.index = self.jump(self.index, code_to_run)
            else:
                self.index = self.nop(self.index)
            if self.index == len(code_to_run): 
                # For part two - exit when the final line has been run.
                return True
        return False
    
    def fix_code(self) -> int:
        """
        create a temporary version of the code and repeatedly switch one
        jmp for nop (or vice versa) until the code runs to the end
        """
        index_changed = []
        code_fixed = False
        while not code_fixed:
            self.reset()
            if len(index_changed) == 0:
                temp_index = 0
            else:
                temp_index = index_changed[-1]+1
            while self.temp_code[temp_index][0] not in ['jmp', 'nop']:
                temp_index += 1
            index_changed.append(temp_index)
            if self.temp_code[temp_index][0] == 'nop':
                if self.temp_code[temp_index][1] != 0:
                    self.temp_code[temp_index] = ('jmp', self.temp_code[temp_index][1])
                else:
                    continue
            elif self.temp_code[temp_index][0] == 'jmp':
                self.temp_code[temp_index] = ('nop', self.temp_code[temp_index][1])
            code_fixed = self.test_code(self.temp_code)
        return self.acc

# run tests
test_program = Code(read_input('inputs/day8_test.txt'))
test_program.test_code(test_program.code)
assert test_program.acc == 5, f"Accumulator is {test_program.acc}, should be 5"
assert test_program.fix_code() == 8, f"Accumulator is {test_program.acc}, should be 8"
print("Tests complete\n\nDAY 8 SOLUTION")

# Part one - run the code until reaching a duplicate row, then print current value of accumulator
program = Code(read_input('inputs/day8.txt'))
program.test_code(program.code)
print(program.acc)

# Part two - keep tweaking the code until it runs to the last line.
fixed_acc = program.fix_code()
print(fixed_acc)
