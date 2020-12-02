# Day 2 - Password Philosphy

# read input file

with open("inputs/day2.txt") as f:
    # create list of policies and passwords
    policy_passwords = [line.split(': ') for line in f.read().splitlines()]
    
    
# Part one - count valid passwords based on policy being number of given letter allowed.
valid_pws = 0

# iterate through lists
for [pol, pw] in policy_passwords:
    count, letter = pol.split(' ')
    [min_count, max_count] = [int(x) for x in count.split('-')]
    # count occurence of letter in password
    counter = pw.count(letter)
    if counter >= min_count and counter <= max_count:
        valid_pws += 1
        
print(valid_pws)

# Part two - policy now describes index of letter (one index is allowed to hold letter)
# indexing starts at 1!!!!!!!!!!!

valid_pws = 0

for [pol, pw] in policy_passwords:
    count, letter = pol.split(' ')
    [min_index, max_index] = [int(x)-1 for x in count.split('-')]
    # if only one of the indices is the letter, add 1 to valid password count
    if (pw[min_index] == letter) is not (pw[max_index]== letter):
        valid_pws += 1

print(valid_pws)
