# Day 13
from funcs import read_input

earliest, bus_numbers = read_input('inputs/day13.txt')
earliest = int(earliest)

class Bus:
    def __init__(self, id):
        self.depart_times = [0]
        self.id = id
        while self.depart_times[-1] < earliest:
            self.depart_times.append(self.depart_times[-1] + id)
        self.earliest_depart = self.depart_times[-1]

bus_numbers = [Bus(int(bus)) for bus in bus_numbers.split(',') if bus != 'x']

print("Part one")

earliest_bus = bus_numbers[-1].earliest_depart

for bus in bus_numbers:
    if bus.earliest_depart < earliest_bus:
        bus_to_take = bus
        
wait = bus_to_take.earliest_depart - earliest

print(f"Earliest departure is bus number {bus_to_take.id} at {bus_to_take.earliest_depart} so the wait is {wait}.")

print(f"Solution is {wait * bus_to_take.id}")