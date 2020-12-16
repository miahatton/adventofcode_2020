# Day 16
from typing import List, Dict

with open('inputs/day16.txt') as f:
    rules, ticket, nearby_tickets = f.read().split('\n\n')
    
rules = {k: v.split(' or ') for k, v in [rule.split(': ') for rule in rules.split('\n')]}
ticket = ticket.split('\n')[1].split(',')
nearby_tickets = [t.split(',') for t in nearby_tickets.split('\n')[1:]]

for k, v in rules.items():
    # give rules format {rule: [[min, max], [min, max]]}
    rules[k][0] = [int(x) for x in rules[k][0].split('-')]
    rules[k][1] = [int(x) for x in rules[k][1].split('-')]

invalid_count = 0


def check_validity(val: int, rules: Dict[str, List], part = 1) -> int:
    validity_count = len(rules.keys())
    valid_fields = []
    for k, rule in rules.items():
        if val > rule[0][1] and val < rule[1][0]:
            validity_count -= 1
        if val < rule[0][0] or val > rule[1][1]:
            validity_count -= 1
        else:
            if part == 2:
                valid_fields.append(k)
    if part == 1:
        if validity_count == 0:
            return False
        else:
            return True
    else:
        return valid_fields

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
    for val in nearby_tickets[i]:
        val = int(val)
        if check_validity(val, rules):
            valid_tickets.append(ticket)

# track which field could be which
fields = []

print(valid_tickets[0])

for ticket in valid_tickets:
    valid_fields = []
    for val in ticket:
        val = int(val)
        valid_fields.append(check_validity(val, rules, 2))
    fields.append([valid_fields])

test_row = fields[0]

