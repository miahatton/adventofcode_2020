from day4_funcs import read_input, check_passports

passports = read_input('inputs/day4.txt')

# Part one - just count the valid passports
print(check_passports(passports, 1))

# Part two - check values as well as fields
print(check_passports(passports, 2))