from funcs import read_input

adapters = sorted(read_input('inputs/day10.txt', convert_to_int = True))

socket = 0
diffs = []

for a in adapters:
    diffs.append(a - socket)
    socket = a

diffs.append(3)

print(diffs.count(1) * diffs.count(3))    