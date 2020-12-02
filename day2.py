# Day 2 - Password Philosphy

# read input file

with open("inputs/day2.txt") as f:
    # create dictionary of policies and passwords
    policy_passwords = [line.split(':') for line in f.readlines()]
    
valid_pws = 0

# iterate through dictionary
for [pol, pw] in policy_passwords:
    pw = pw.replace('\n', '')
    count, letter = pol.split(' ')
    [min_count, max_count] = [int(x) for x in count.split('-')]
    # count occurence of letter in password
    counter = pw.count(letter)
    if counter >= min_count and counter <= max_count:
        valid_pws += 1
        
print(valid_pws)
    
