from funcs import read_input
import numpy as np

# Day 11
seats = read_input('inputs/day11_test.txt')
rows = []
for seat_row in seats:
    this_row = []
    for char in seat_row:
        this_row.append(char)
    rows.append(this_row)

seat_array = np.array(rows)
    
print(seat_array)

def list_surrounds(seat_array, i, j):
    surround_pairs =  [(j+1, i-1), (j+1, i), (j+1, i+1), 
                       (j, i-1), (j, i+1), 
                       (j-1, i-1), (j-1, i), (j-1, i+1)]
    surrounding_seats = []
    for pair in surround_pairs:
        try:
            surrounding_seats.append(seat_array[pair[0], pair[1]])
        except IndexError:
            continue
    return surrounding_seats

def occupy(seat_array):
    new_array = seat_array.copy()
    for j in range(seat_array.shape[0]): # loop through row numbers
        for i in range(seat_array.shape[1]): # loop through column numbers
            if seat_array[j, i] == '.':
                new_array[j, i] = seat_array[j, i] 
                continue # ignore the floor
            # list surrounding seats
            surround = list_surrounds(seat_array, i, j)
            if seat_array[j,i] == 'L':
                if surround.count('#') == 0:
                    new_array[j, i] = '#'
                else:
                    new_array[j, i] = 'L'
            elif seat_array[j, i] == '#':
                if surround.count('#') >= 4:
                    new_array[j, i] = 'L'
                else:
                    new_array[j, i] = '#'
    return new_array
        
print()
new_array = occupy(seat_array)
print(new_array)
print()
print(occupy(new_array))