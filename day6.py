# Day 6
from funcs import read_input

# read input
part_two_answers = read_input('inputs/day6.txt', sep = '\n\n')

# join individual answers together into a single string per group for part one
part_one_answers = [
        line.replace('\n', '') for line in 
        part_two_answers
    ]

# Part one solution

# count number of unique characters in each group string
total_answers = sum([len(set(group)) for group in part_one_answers])

print(total_answers)

#Part two solution

total_answered_by_all = 0

# loop through each group
for group in part_two_answers:
    # get unique characters for each group
    for q in set(group.replace('/n', '')):
        # if the number of occurences equals the number of people, add one to final count
        if group.count(q) == len(group.split('\n')):
            total_answered_by_all += 1
            
print(total_answered_by_all)