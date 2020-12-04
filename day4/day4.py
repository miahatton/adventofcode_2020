from day4_funcs import read_input, check_passports
from day4_tests import test_year_validity, test_height_validity, test_colour_validity, test_pid_validity, test_passports

# Check that tests pass
test_year_validity()
test_height_validity()
test_colour_validity()
test_pid_validity()
test_passports(read_input('inputs/valid_passports.txt'), True)
test_passports(read_input('inputs/invalid_passports.txt'), False)
    
# read input
passports = read_input('inputs/day4.txt')
    
# Part one - just count the valid passports
print(check_passports(passports, 1))
    
# Part two - check values as well as fields
print(check_passports(passports, 2))