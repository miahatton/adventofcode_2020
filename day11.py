from funcs import read_input
import numpy as np

def list_surrounds(seat_array: np.ndarray, i: int, j: int) -> np.ndarray:
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


def surrounding_seats(seat_array, i, j, part_num):
    # we want to try every combination of i, i+1, i-1, j, j+1, j-1 and track which operations we've done!
    seats = []
    ops = [(1, -1), (+1, 0), (1, 1), (0, -1), (0, 1), (-1,-1), (-1,0), (-1,1)]
    for op in ops:
        temp = [j + op[0],i + op[1]]
        while temp[1] >= 0 and temp[0] >= 0:
            try:
                if seat_array[temp[0], temp[1]] != '.':
                    seats.append(seat_array[temp[0], temp[1]])
                    break
                elif part_num == 2:
                    temp[0] += op[0]
                    temp[1] += op[1]
                else:
                    break
            except IndexError:
                break
    return seats

def occupy(seat_array: np.ndarray, part_num: int) -> np.ndarray:
    if part_num == 1:
        thresh = 4
    else:
        thresh = 5
    new_array = np.empty((seat_array.shape[0], seat_array.shape[1]), dtype = str)
    for j in range(seat_array.shape[0]): # loop through row numbers
        for i in range(seat_array.shape[1]): # loop through column numbers
            if seat_array[j, i] == '.':
                new_array[j, i] = seat_array[j, i] 
            else:
                # list surrounding seats
                surround = surrounding_seats(seat_array, i, j, part_num)
                # count occupied around unoccupied
                if seat_array[j,i] == 'L' and surround.count('#') == 0:
                        new_array[j, i] = '#'
                # count unoccupied around occupied
                elif seat_array[j, i] == '#' and surround.count('#') >= thresh:
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

# select part number when calling occupy function
while not np.array_equal(seat_array, occupy(seat_array, 2)):
    seat_array = occupy(seat_array, 2)
    
print(np.count_nonzero(seat_array == '#'))