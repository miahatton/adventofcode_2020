from funcs import read_input
import re

ingredients_allergens = read_input('inputs/day21_test.txt')

ingredients = [line.split(' (')[0] for line in ingredients_allergens]
allergens = [re.search('\(.+\)', line).group(0)[10:-1] for line in ingredients_allergens]

print(ingredients)
print(allergens)