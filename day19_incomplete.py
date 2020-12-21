from funcs import read_input
import re

messages = read_input('inputs/day19_test.txt')
rules = {int(i): r for i, r in [m.split(': ') for m in messages[:messages.index('')]]}
messages = messages[messages.index('')+1:]

for k,v in sorted(rules.items(), key = lambda x: x[0]):
    if re.search("[a-z]", v):
        rules[k] = re.search("[a-z]", v).group(0)
    # actually should do this AFTER 
    elif '|' in v:
        rules[k] = [int(num) for num in [
            string.strip().split(' ') for string in v.split('|')]
            ]
    else:
        rules[k] = [v.strip()]
        rules[k] = [seq.split(' ') for seq in rules[k]]
    print(k, ": ", v)
    print(k, ": ", rules[k])
    
    
def count_nums_in_rule(rule):
    count_nums = 0
    for i in range(len(rule)):
        # each list within rules[0] is an allowed sequence
        for pos in rule[i]:
            if re.search('\d', pos):
                count_nums += 1
    return count_nums

def what_are_the_rules(rules, rule_key):
    print(rule_key)
    rule_key = int(rule_key)
    nums_left_0 = count_nums_in_rule(rules[int(rule_key)])
    while nums_left_0 > 0:
        new_rule = []
        for i in range(len(rules[rule_key])):
            new_subrule = []
            for j in range(len(rules[rule_key][i])):
                new_subrule.append(what_are_the_rules(rules, rules[rule_key][i][j]))
            new_rule.append(new_subrule)
        rules[rule_key] = new_rule
    return rules[rule_key]
            
print(what_are_the_rules(rules, 0))
    