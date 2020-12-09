# DAY 9
from funcs import read_input


# switch between test data and real data
test = False

# set filename and length of preamble list
if test:
    file = 'inputs/day9_test.txt'
    preamble_len = 5
else:
    file = 'inputs/day9.txt'
    preamble_len = 25

# read input data
data = read_input(file, '\n', True)

# get preamble numbers
preamble = []

# initiate preamble
for i in range(preamble_len):
    preamble.append(data.pop(0))

# continuously shift numbers from data to preamble and 
# look for numbers in the preamble that sum to the first number in data
while True:
    target = data[0]
    for i, num in enumerate(preamble[:-1]):
        diff = target - num
        if diff == target and preamble.count(diff)<2:
            continue
        if diff in preamble[i+1:]:
            preamble.pop(0)
            preamble.append(data.pop(0))
            break
    else:
        # if no numbers are found that sum to the first number in data, break the loop
        break
            
invalid_num = data[0]
print(f'Part one: invalid number is {invalid_num}')

# refresh data
data = read_input(file, '\n', True)

# iterate through data and sum numbers in sequence until the sum = the invalid number
for i in range(len(data)):
    sum = data[i]
    j = 1
    try:
        while sum < invalid_num:
            # add numbers until they sum to at least invalid number
            sum += data[i+j]
            j+=1
        if sum == invalid_num:
            # found the sequence!
            seq = data[i:i+j]
            solution = max(seq) + min(seq)
            break
    except IndexError:
        print("END OF THE ROAD MATE")
    
print(solution)
        