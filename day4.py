import re

# read input

with open('inputs/day4.txt', 'r') as f:
    passports = [
            {
                field: val for field, val in 
                # split pairs at the colon, split list into pairs at spaces
                [pair.split(':') for pair in passport.split(' ')]
            } for passport in 
                # split double new lines and replace single new lines with spaces
                [x.replace('\n',' ') for x in f.read().split('\n\n')]
        ]

# Part one - just count the valid passports
valid_passports = []

for passport in passports:
    # if all fields are present or if all except cid are present, add to list
    if (len(passport.keys()) == 8) or (len(passport.keys()) == 7 and 'cid' not in passport.keys()):
        valid_passports.append(passport)

print(len(valid_passports))


# Part two - check values as well as fields

count_valid = 0

def year_validity_check(year: str, field: str) -> bool:
    if not re.match('\d{4}', year):
        return False
    elif field == 'byr' and int(year) >= 1920 and int(year) <= 2002:
        return True
    elif field == 'iyr' and int(year) >= 2010 and int(year) <= 2020:
        return True
    elif field == 'eyr' and int(year) >= 2020 and int(year) <= 2030:
        return True
    else:
        return False

def height_validity_check(height: str) -> bool:
    if not re.match(r'\d+(cm|in)', height):
        return False
    num = int(height[:-2])
    if height[-2:] == 'cm' and num >= 150 and num <= 193:
        return True
    elif height[-2:] == 'in' and num >= 59 and num <= 76:
        return True
    else:
        return False

def colour_validity_check(color: str, field: str) -> bool:
    if field == 'ecl' and color in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return True
    elif field == 'hcl' and re.match('#[a-z0-9]{6}', color):
        return True
    else:
        return False

for passport in valid_passports:
    checks = [
        year_validity_check(passport['byr'], 'byr'), year_validity_check(passport['iyr'], 'iyr'), year_validity_check(passport['eyr'], 'eyr'),
        height_validity_check(passport['hgt']), colour_validity_check(passport['hcl'], 'hcl'), colour_validity_check(passport['ecl'], 'ecl'),
        re.match(r'\d{9}', passport['pid'])
    ]
    if all(checks):
        count_valid += 1

print(count_valid)