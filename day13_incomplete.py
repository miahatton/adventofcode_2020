# Day 13
from funcs import read_input

earliest, bus_numbers = read_input('inputs/day13.txt')
earliest = int(earliest)
bus_numbers = [int(bus) for bus in bus_numbers.split(',') if bus != 'x']

bus_timings = [0] * len(bus_numbers) # used to add timestamp in loop
first_bus = [0] * len(bus_numbers) # store the first bus after the departure time for each id


bus_numbers_to_try = list(range(0, len(bus_numbers))) # store indexes


while len(bus_numbers_to_try) > 0:
    for i in bus_numbers_to_try:
        bus_timings[i] += bus_numbers[i]
        if bus_timings[i] > earliest:
            bus_numbers_to_try.remove(i)
    print(bus_timings)

bus_to_take = first_bus.index(min(first_bus))

print((bus_timings[bus_to_take] - earliest) * bus_numbers[bus_to_take])