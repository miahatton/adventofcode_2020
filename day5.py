from funcs import read_input
import numpy as np

class Ticket:
    def __init__(self, code: str):
        self.boarding_pass = code
        self.binary_row = code[:-3].replace('F', '0').replace('B', '1')
        self.binary_col = code[-3:].replace('L', '0').replace('R', '1')
        self.row_num = 0
        self.col_num = 0
        self.id = 0
    def binary_converter(self, bin_num: str) -> int:
        dec_num = 0
        x = 1
        for i in range(len(bin_num)-1, -1, -1):
            dec_num += x * int(bin_num[i])
            x *= 2
        return dec_num
    def solve(self) -> int:
        self.row_num = self.binary_converter(self.binary_row)
        self.col_num = self.binary_converter(self.binary_col)
        self.id = 8 * self.row_num + self.col_num
        return self.id
        
def test_binary_converter():
    for test_ticket, row, col in zip(['FBFBBFFRLR', 'BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL'], [44, 70, 14, 102], [5,7,7,4]):
        ticket = Ticket(test_ticket)
        ticket_id = ticket.solve()
        assert ticket.row_num == row, f"Ticket {ticket.boarding_pass} should have row {row}, returns {ticket.row_num}"
        assert ticket.col_num == col, f"Ticket {ticket.boarding_pass} should have column {col}, returns {ticket.col_num}"
        assert ticket_id == 8*row + col, f"Ticket {ticket.boarding_pass} should have id {8*row + col}, returns {ticket.id}"

# check that tests pass
test_binary_converter()

# for part two - create grid of seats
plane = np.zeros((128,8))
seat_ids = []

# read input
first = True
for line in read_input('inputs/day5.txt'):
    ticket = Ticket(line)
    ticket_id = ticket.solve()
    seat_ids.append(ticket_id)
    plane[ticket.row_num, ticket.col_num] = 1

max_id = max(seat_ids)

print(f'The highest ticket ID is {max_id}')

# Part two: which seats are left?

your_seat = []

for i in range(0, plane.shape[0]):
    row = []
    for j in range(0, plane.shape[1]):
        if plane[i,j] == 0:
            row.append([i,j])
    if len(row) == 1:
        your_seat = row[0]

print(f'Your seat id is {your_seat[0] * 8 + your_seat[1]}')