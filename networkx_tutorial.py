##### NETWORKX TUTORIAL #########
import re
import networkx as nx
from funcs import read_input
from typing import List, Dict

lines = read_input('inputs/day7_test.txt')

def parse_bag(bag_desc) -> (str, int):
    count = int(re.search('\d+', bag_desc).group(0))
    color = re.sub('\d+ ', '', re.sub(' bags?', '', bag_desc))
    return (color, count)

def parse_lines(lines: List[str]) -> Dict:
    bag_dict = dict()
    for line in lines:
        outer, inner = line.split(' bags contain ')
        if 'no' in inner:
            inner_bags = []
        else:
            inner_bags = [
                    parse_bag(bag.replace('.', '')) for bag in inner.split(', ')
                ]
        if outer in bag_dict.keys():
            bag_dict[outer].append(inner_bags)
        else:
            bag_dict[outer] = inner_bags
        for bag, count in innfer_bags:
            if bag not in bag_dict.keys():
                bag_dict[bag] = [] 
    return bag_dict

G = nx.Graph()

for k, v in parse_lines(lines).items():
    G.add_node(k)
    if len(v)>0:
        for colour, count in v:
            for i in range(count):
                G.add_edge(k, colour)
                
print(G.number_of_nodes())