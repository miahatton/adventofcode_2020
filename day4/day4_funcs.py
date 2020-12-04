import re
from typing import List, Dict

def read_input(file_loc: str) -> List[Dict]:
    """
    Read lines from the input file, split into dictionaries of field/value pairs
    Return list of dictionaries
    """
    with open(file_loc, 'r') as f:
        passports = [
                {
                    field: val for field, val in 
                    # split pairs at the colon, split list into pairs at spaces
                    [pair.split(':') for pair in passport.split(' ')]
                } for passport in 
                    # split double new lines and replace single new lines with spaces
                    [x.replace('\n',' ') for x in f.read().split('\n\n')]
            ]
    return passports

def year_validity_check(year: str, field: str) -> bool:
    """
    Check that the year is valid, i.e. 4 digits and within specified timeframe
    """
    if not re.match('\d{4}', year):
        return False
    # Birth year between 1920 and 2002
    elif field == 'byr' and int(year) >= 1920 and int(year) <= 2002:
        return True
    # Year of issue between 2010 and 2020
    elif field == 'iyr' and int(year) >= 2010 and int(year) <= 2020:
        return True
    # Year of expiry between 2020 and 2030
    elif field == 'eyr' and int(year) >= 2020 and int(year) <= 2030:
        return True
    else:
        return False

def height_validity_check(height: str) -> bool:
    """
    Check that height is valid i.e. digits followed by cm or in, within specified range
    """
    if not re.match(r'\d+(cm|in)', height):
        return False
    # extract digits
    num = int(height[:-2])
    if height[-2:] == 'cm' and num >= 150 and num <= 193:
        return True
    elif height[-2:] == 'in' and num >= 59 and num <= 76:
        return True
    else:
        return False

def colour_validity_check(color: str, field: str) -> bool:
    """
    Check that eye or hair colour is valid
    """
    # eye colour must be one of specified values
    if field == 'ecl' and color in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return True
    # hair colour must be valid hex code
    elif field == 'hcl' and re.match('#[a-f0-9]{6}', color):
        return True
    else:
        return False
    
def pid_check(pid: str) -> bool:
    """
    passport id must be a nine digit number
    """
    if re.match(r'[0-9]{9}$', pid) is not None:
        return True
    else:
        return False

def all_checks(passport: Dict) -> bool:
    """
    Perform checks on all fields and return True iff all fields are valid
    """
    checks = [
                year_validity_check(passport['byr'], 'byr'), 
                year_validity_check(passport['iyr'], 'iyr'), 
                year_validity_check(passport['eyr'], 'eyr'),
                height_validity_check(passport['hgt']), 
                colour_validity_check(passport['hcl'], 'hcl'), 
                colour_validity_check(passport['ecl'], 'ecl'),
                pid_check(passport['pid'])
            ]
    return all(checks)

def check_passports(passports: List, part: int) -> int:
    """
    First, loop through passports to check that all required fields are present
    If part == 2, loop through passports with required fields and check validity
    Return count of valid passports for given part.
    """
    valid_passport_fields = []
    # part one
    for passport in passports:
        # if all fields are present or if all except cid are present, add to list
        if (len(passport.keys()) == 8) or (len(passport.keys()) == 7 and 'cid' not in passport.keys()):
            valid_passport_fields.append(passport)
    if part == 1:
        return len(valid_passport_fields)
    count_valid = 0
    for passport in valid_passport_fields:
        if(all_checks(passport)):
                count_valid += 1
    return count_valid

