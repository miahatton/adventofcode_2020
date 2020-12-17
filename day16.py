# Day 16
from typing import List, Dict

with open('inputs/day16.txt') as f:
    rules, ticket, nearby_tickets = f.read().split('\n\n')
    
rules = {k: v.split(' or ') for k, v in [rule.split(': ') for rule in rules.split('\n')]}
my_ticket = ticket.split('\n')[1].split(',')
nearby_tickets = [t.split(',') for t in nearby_tickets.split('\n')[1:]]

for k, v in rules.items():
    # give rules format {rule: [[min, max], [min, max]]}
    rules[k][0] = [int(x) for x in rules[k][0].split('-')]
    rules[k][1] = [int(x) for x in rules[k][1].split('-')]

invalid_count = 0

print(len(nearby_tickets), " tickets.")

def check_validity(val: int, rules: Dict[str, List]) -> int:
    validity_count = len(rules.keys())
    for k, rule in rules.items():
        if val > rule[0][1] and val < rule[1][0]:
            validity_count -= 1
        if val < rule[0][0] or val > rule[1][1]:
            validity_count -= 1
    if validity_count == 0:
        return False
    else:
        return True

# Part One
for ticket in nearby_tickets:
    for val in ticket:
        val = int(val)
        if not check_validity(val, rules):
            invalid_count += val
            continue
          
print("*"*20, " Part One ", "*"*20)
print(invalid_count)
print()
print("*"*20, " Part Two ", "*"*20)

# remove invalid tickets

valid_tickets = []

for i in range(len(nearby_tickets)):
    valid = True
    for val in nearby_tickets[i]:
        if not check_validity(int(val), rules):
            valid = False
    if valid:
        valid_tickets.append(nearby_tickets[i])

# track which field could be which

possible_fields = {}

# put all valid fields into list for each position on the ticket
for i in range(len(valid_tickets[0])):
    # make lists of values for each position
    position = [x[i] for x in valid_tickets]
    # start with all fields
    position_fields = list(rules.keys())
    for val in position:
        for field in rules.keys():
            if field in position_fields:
                # check validity of value against each field
                if not check_validity(int(val), {field: rules[field]}):
                    # remove invalid fields
                    position_fields.pop(position_fields.index(field))
    possible_fields[i] = position_fields

# if any position holds only one field, remove that field from all other positions
# repeat until each position holds only one field
while not all([len(x) == 1 for x in possible_fields.values()]):
    unique = []
    for k, v in sorted(possible_fields.items(), key = lambda x: len(x[1])):
        if len(v) == 1:
            unique.append(v[0])
        else:
            remove = [i for i in range(len(v)) if v[i] in unique]
            for i in remove:
                v.pop(i)
            
departure_fields = 1

for i in range(len(my_ticket)):
    if 'departure' in possible_fields[i][0]:
        departure_fields *= int(my_ticket[i])
        
print(departure_fields)
            