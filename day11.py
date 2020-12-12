from funcs import read_input
import numpy as np

def list_surrounds(seat_array, i, j):
    surround_pairs =  [(j+1, i-1), (j+1, i), (j+1, i+1), 
                       (j, i-1), (j, i+1), 
                       (j-1, i-1), (j-1, i), (j-1, i+1)]
    surrounding_seats = []
    for pair in surround_pairs:
        try:
            if pair[1] != -1 and pair[0] != -1:
                surrounding_seats.append(seat_array[pair[0], pair[1]])
        except IndexError:
            continue
    return surrounding_seats

def occupy(seat_array):
    new_array = np.empty((seat_array.shape[0], seat_array.shape[1]), dtype = str)
    for j in range(seat_array.shape[0]): # loop through row numbers
        for i in range(seat_array.shape[1]): # loop through column numbers
            if seat_array[j, i] == '.':
                new_array[j, i] = seat_array[j, i] 
                continue # ignore the floor
            # list surrounding seats
            else:
                surround = list_surrounds(seat_array, i, j)
                if seat_array[j,i] == 'L' and surround.count('#') == 0:
                        new_array[j, i] = '#'
                elif seat_array[j, i] == '#' and surround.count('#') >= 4:
                        new_array[j, i] = 'L'
                else:
                    new_array[j, i] = seat_array[j,i]
    return new_array

# Day 11
seats = read_input('inputs/day11.txt')
rows = []
for seat_row in seats:
    this_row = []
    for char in seat_row:
        this_row.append(char)
    rows.append(this_row)
    
seat_array = np.array(rows)

while not np.array_equal(seat_array, occupy(seat_array)):
    seat_array = occupy(seat_array)
    
print(np.count_nonzero(seat_array == '#'))