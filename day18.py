# day 18
import re
from funcs import read_input
from typing import List

def deal_with_brackets(problem, partnum: int) -> str:
    """
    Replace (expression) with result of evaluation expression. 
    Return problem without brackets.
    """
    expression = re.search("\([^\(\)]+\)", problem).group(0)
    inside_bracket = str(do_math(expression[1:-1], partnum))
    return problem.replace(expression, inside_bracket)

def perform_addition(problem: str) -> str:
    """
    Split input at each "n + m", replace with the sum of n and m. Return input.
    """
    expression = re.search("\d+ \+ \d+", problem).group(0)
    before, after = problem.split(expression, maxsplit = 1)
    new_val = sum([int(x) for x in expression.split(' + ')])
    return before + str(new_val) + after

def reduce_math(problem, partnum: int) -> str:
    """
    Reduce problem to a new string without any bracket expressions.
    If partnum == 2 also perform all addition evaluations.
    """
    while "(" in problem:
        problem = deal_with_brackets(problem, partnum)
    if partnum == 2:
        while "+" in problem:
            problem = perform_addition(problem)
    return problem

def get_acc_and_remove(problem: str) -> (int, str):
    """
    Initialise the accumulator as the first digit in the expression. 
    Remove this digit from the expression.
    """
    acc = int(re.match('\d+', problem).group(0))
    problem = problem[len(str(acc))+1:]
    return acc, problem

def get_next_op(problem) -> (bool, str):
    """
    If the expression begins with an operator, return the operator and following digit.
    """
    try:
        return True, re.match('(\*|\+) \d+ ?', problem).group(0)
    except AttributeError:
        return False, None

def do_math(problem: str, partnum: int) -> int:
    """
    Perform all arithmetical operations as instructed in this line of the homework (problem).
    """
    problem = reduce_math(problem, partnum)
    acc, problem = get_acc_and_remove(problem)
    should_continue, next_operation = get_next_op(problem)
    # if there is another operator, continue performing arithmetic operations
    while should_continue:
        if partnum == 1:
            # use operator and remove
            ops = next_operation.split(' ')
            if '+' in next_operation:
                acc += int(ops[1])
            elif '*' in next_operation:
                acc *= int(ops[1])
        else:
            # use operator and remove
            ops = next_operation.split(' ')
            acc *= int(ops[1])
        # remove the operation from the problem
        problem = problem[len(next_operation):]
        # get next operation
        should_continue, next_operation = get_next_op(problem)
    return acc

def do_my_homework(homework: List[str], partnum: int) -> int:
    """
    Loop through each expression in the list and evaluate to a single integer.
    Add the integers together while looping.
    """
    total = 0
    for line in homework:
        if partnum == 2:
            print(line)
            print(do_math(line, partnum))
        total += do_math(line, partnum)
    return total
  
def run_tests():  
    test_inputs = [
        "1 + (2 * 3) + (4 * (5 + 6))",
        "2 * 3 + (4 * 5)", 
        "5 + (8 * 3 + 9 + 3 * 4 * 3)", 
        "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))",
        "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"
            ]
    solutions_1 = [51, 26, 437, 12240, 13632]
    solutions_2 = [51, 46, 1445, 669060, 23340]
    for i in range(len(test_inputs)):
        assert do_math(test_inputs[i], 1) == solutions_1[i], f"Part one: {test_inputs[i]} should evaluate to {solutions_1[i]}"
        assert do_math(test_inputs[i], 2) == solutions_2[i], f"Part two: {test_inputs[i]} should evaluate to {solutions_2[i]}"
    print("Tests passed")

math_homework = read_input('inputs/day18.txt')
run_tests()
part_one = do_my_homework(math_homework, 1)    
print("Part one solution: ", part_one)
part_two = do_my_homework(math_homework, 2)
print("Part two solution: ", part_two)



