from funcs import read_input
from typing import List

class Code:
    
    code = []
    temp_code = []
    
    def __init__(self, input_strings: List):
        self.input_strings = input_strings
        self.code = self.read_input_strings()
        self.reset()
        
    def read_input_strings(self):
        return [
                (ins, int(step)) for ins, step in 
                [line.split(' ') for line in self.input_strings]
                ]
        
    def reset(self):
        self.index = 0
        self.acc = 0
        self.index_run = []
        self.temp_code = self.read_input_strings()
        
    def print_code(code):
        for line in code:
            print(line)
        
    def append_index(self):
        self.index_run.append(self.index)
        
    def accumulator(self, i, code_to_run):
        self.acc += code_to_run[i][1]
        self.append_index()
        return i + 1
    
    def jump(self, i, code_to_run):
        self.append_index()
        return i + code_to_run[i][1]
    
    def nop(self, i):
        self.append_index
        return i + 1
    
    def test_code(self, code_to_run):
        while self.index not in self.index_run:
            print('\t'.join([str(x) for x in code_to_run[self.index]]))
            if code_to_run[self.index][0] == 'acc':
                self.index = self.accumulator(self.index, code_to_run)
            elif code_to_run[self.index][0] == 'jmp':
                self.index = self.jump(self.index, code_to_run)
            else:
                self.index = self.nop(self.index)
            if self.index == len(code_to_run) - 1:
                return True
        return False
    
    def fix_code(self):
        index_changed = []
        code_fixed = False
        while not code_fixed:
            self.reset()
            print(self.code)
            for line in self.temp_code:
                print(line)
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
        
    


program = Code(read_input('inputs/day8.txt'))
program.test_code(program.code)
print(program.acc)

fixed_acc = program.fix_code()
print(fixed_acc)