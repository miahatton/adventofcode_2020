# day 18
import re
from funcs import read_input

math = read_input('inputs/day18_test.txt')

def do_math(input_line: str):
    print("input_line: ", input_line)
    while "(" in input_line:
        inside_bracket = str(do_math(re.search("\(.+\)", input_line).group(0)[1:-1]))
        input_line = re.sub("\(.+\)", inside_bracket, input_line)
        print("input_line: ", input_line)
    acc = int(re.match('\d+', input_line).group(0))
    input_line = input_line[len(str(acc))+1:]
    print("input_line: ", input_line)
    next_operation = re.match('(\*|\+) \d+ ?', input_line).group(0)
    print("next_operation: ", next_operation)
    while next_operation:
        # use operator and remove
        ops = next_operation.split(' ')
        print(ops)
        if '+' in next_operation:
            acc += int(ops[1])
        elif '*' in next_operation:
            acc *= int(ops[1])
        print("acc: ", acc)
        input_line = input_line[len(next_operation):]
        print("input_line: ", input_line)
        # get next operation
        try:
            next_operation = re.match('(\*|\+) \d+ ?', input_line).group(0)
            print(next_operation)
        except AttributeError:
            break
    print("acc: ", acc)
    return acc

assert do_math("2 * 3 + (4 * 5)") == 26, "Should evaluate to 26"
assert do_math("5 + (8 * 3 + 9 + 3 * 4 * 3)") ==437, "Should becomes 437."
assert do_math("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))") == 12240, "Should become 12240."
assert do_math("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2") == 13632, "Should become 13632."
