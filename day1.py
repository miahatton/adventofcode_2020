# Read input
with open("inputs/day1.txt") as f:
    expenses = [int(num) for num in f.readlines()]

def find_solution():
    # loop through each entry and add to each other entry
    for i in range(len(expenses)):
        for j in range(len(expenses)):
            if i==j:
                continue
            #... until we find two that sum to 2020
            elif expenses[i] + expenses[j] == 2020:
                return expenses[i]*expenses[j]

print(find_solution())

# Part two

def find_solution_two():
    # loop through each entry and add to each other entry
    for i in range(len(expenses)):
        for j in range(len(expenses)):
            if i==j:
                continue
            for k in range(len(expenses)):
                if i == k or j == k:
                    continue
                #... until we find three that sum to 2020
                elif expenses[i] + expenses[j] + expenses[k] == 2020:
                    return expenses[i]*expenses[j]*expenses[k]
                
print(find_solution_two())
