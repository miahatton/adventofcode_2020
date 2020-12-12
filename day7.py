from funcs import read_input
from typing import List, Dict, Set
from collections import defaultdict
import re

def extract_bag_colours(bag_desc: str, need_numbers = False) -> List:
    """
    Turn string list of bags into actual list of bags,
    remove numbers and word 'bag'
    """
    bag_desc = bag_desc.replace('.', '')
    bags = []
    for bag in bag_desc.split(', '):
        bag_color = re.sub('\d+', '',
                           re.sub('bags?', '', bag)).strip()
        if need_numbers:
            count = re.search('\d+', bag).group(0)
            bags.append((bag_color, int(count)))
        else:
            bags.append(bag_color)
    return bags
    
def sort_bags(rules: List[str], list_contents = False) -> Dict:
    bags = defaultdict(list)
    for rule in rules:
        outer_bag, inner_bags = rule.split('s contain ')
        contents = extract_bag_colours(inner_bags, need_numbers = list_contents)
        for bag in contents:
            if not list_contents:
                bags[bag].append(outer_bag.replace(' bag', ''))
            else: 
                bags[outer_bag.replace(' bag', '')].append(bag)
    return bags

def list_holders(color: str, bag_holders: Dict) -> Set:
    contains_color = set(bag_holders[color])
    for col in contains_color:
        contains_color = contains_color.union(list_holders(col, bag_holders))
    return set(contains_color)

def list_contents(color: str, bag_contents: Dict, count = 1, recur = False) -> Set:
    inside_color = set([(col[0], col[1]*count) for col in bag_contents[color]])
    if recur:
        print("Recursion time!\t", f"count = {count}\tColor is {color}")
    for bag, count in inside_color:
        print(bag, count)
    print(' ')
    for col, n in inside_color:
        inside_color = inside_color.union(list_contents(col, bag_contents, n, True))
    return inside_color

lines = [
    line for line in read_input('inputs/day7.txt') if not re.search("no other bags", line)
]

print('How many bags can hold the shiny gold bag?')
bag_holders = sort_bags(lines)
print(len(list_holders('shiny gold', bag_holders)))

contents = sort_bags(lines, True)

print("How many bags are inside the shiny gold bag?")    

group_bags = {}

for bag, count in list_contents('shiny gold', contents):
    print(bag, count)
    if bag not in group_bags.keys():
        group_bags[bag] = count
    else:
        group_bags[bag] += count

print(sum(group_bags.values()))