class RowOfTrees:
    def __init__(self, pattern):
        self.pattern = pattern
    def extend(self):
        # repeat the pattern as many times as needed
        self.pattern += self.pattern

# get input
with open('inputs/day3.txt', 'r') as f:
    patterns = f.read().splitlines()

def count_trees(input_strings, right, down):
    # list of RowOfTrees objects
    rows_of_trees = []
    for pattern in input_strings:
        rows_of_trees.append(RowOfTrees(pattern))

    # starting position
    pos = [0,0]

    # tree counter
    trees = 0

    # loop through rows
    while pos[0] < len(rows_of_trees): # start at position 0
        # is it a tree?
        checking = True
        while checking:
            try:
                char = rows_of_trees[pos[0]].pattern[pos[1]]
                checking = False
            except IndexError:
                # extend the row if no characters found at the position
                rows_of_trees[pos[0]].extend()
        if char ==  '#':
            trees += 1
        # move
        pos[1] += right
        pos[0] += down
    
    return trees

# Part one solution
print("Part one solution: ")
print(count_trees(patterns, 3, 1))

print('\n','*' * 20, '\n', sep='')

# Part two solution
slopes = zip([1,3,5,7,1], [1,1,1,1,2])
tree_counts_product = 1

for right, down in slopes:
    tree_counts_product *= count_trees(patterns, right, down)

print("Part two solution:")
print(tree_counts_product)