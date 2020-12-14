# day 14
from funcs import read_input
import re

class Memory:
    def __init__(self):
        self.memory_used = {}
        self.dec_memory = 0
        self.mask = "X" * 36
    def set_mask(self, new_mask):
        self.mask = new_mask
    def binary_converter(self, bin_num: str) -> int:
        dec_num = 0
        x = 1
        for i in range(len(bin_num)-1, -1, -1):
            dec_num += x * int(bin_num[i])
            x *= 2
        return dec_num
    def apply_mask(self, dec_num: str) -> str:
        # TODO convert dec_num to bin_num
        bin_num = str(dec_num)
        chars = [char for char in bin_num]
        for i in range(36):
            if self.mask[i] != 'X':
                chars[i] = self.mask[i]
        return ''.join(chars)
    def set_memory(self, pos, bin_num):
        bin_masked = self.apply_mask(bin_num)
        self.memory_used[pos] = bin_masked
    def calculate_memory_total(self):
        for _, v in self.memory_used.items():
            self.dec_memory += self.binary_converter(v)
        print(self.dec_memory)
        
instructions = [line.split(" = ") for line in read_input('inputs/day14_test.txt')]
        
memory = Memory()
    
for line in instructions:
    if line[0] == 'mask':
        memory.mask = line[1]
    else:
        position = re.search('\d+', line[0]).group(0)
        memory.set_memory(position, line[1])
        
for k, v in memory.memory_used.items():
    print(f'{k}:\t{v}')
        
memory.calculate_memory_total()
        
