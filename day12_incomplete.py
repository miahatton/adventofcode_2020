from funcs import read_input

class Ship:
    def __init__(self):
        self.manhattan = [0,0] # east and north are positive
        self.direction = 0  # E = 0, S = 90, W = 180, N = 270
        self.position = {0: 0, 90: 0, 180: 0, 270: 0}
        self.direction_map = dict(E = 0, S = 90, W = 180, N = 270)
        self.x_pos = []
        self.y_pos = []
    def change_direction(self, rotate_dir: str, degrees: int):
        while degrees > 0:
            if rotate_dir == 'R':
                self.direction += 90
                if self.direction == 360:
                    self.direction = 0
            else:
                self.direction -= 90
                if self.direction < 0:
                    self.direction = 270
            degrees -= 90
    def move(self, direction_in_instruction: str, distance: int):
        if direction_in_instruction != 'F':
            movement_dir = self.direction_map[direction_in_instruction]
        else:
            movement_dir = self.direction
        self.position[movement_dir] += distance
    def calculate_manhattan(self):
        self.manhattan[0] = abs(self.position[0] - self.position[180])
        self.manhattan[1] = abs(self.position[90] - self.position[270])
    def read_instruction(self, step: int):
        if step[0] in ['R', 'L']:
            self.change_direction(step[0], int(step[1:]))
        else:
            self.move(step[0], int(step[1:]))
            
class ShipWithWaypoint(Ship):
    def __init__(self):
        super().__init__()
        self.set_waypoint()
    def set_waypoint(self):
        self.waypoint_pos = {
                0: self.position[0] + 10,
                90: self.position[90],
                180: self.position[180],
                270: self.position[270] + 1
            }
    def change_direction(self, rotate_dir: str, degrees: int):
        map_left_rotate = {0: 90, 90: 180, 180: 270, 270: 0}
        map_right_rotate = {0: 270, 90: 0, 180: 90, 270: 180}
        mapping = map_right_rotate if rotate_dir == 'R' else map_left_rotate
        new_waypoint_dir = self.waypoint_pos.copy()
        for key in new_waypoint_dir.keys():
            new_waypoint_dir[key] = self.waypoint_pos[mapping[key]]
        self.waypoint_pos = new_waypoint_dir
    def move(self, direction_in_instructions: str, distance: int):
        if direction_in_instructions == 'F':
            for key in self.waypoint_pos.keys():
                self.position[key] += self.waypoint_pos[key] * distance
        else:
            movement_dir = self.direction_map[direction_in_instructions]
            self.waypoint_pos[movement_dir] += distance
    def update_position(self):
        self.x_pos.append(self.position[180] - self.position[0])
        self.y_pos.append(self.position[270] - self.position[90])


instructions = read_input('inputs/day12.txt')

ship = ShipWithWaypoint()
print("Ship position: ", end = '\t\t')
print(ship.position)
print("Waypoint position: ", end = '\t')
print(ship.waypoint_pos)
print()

i = 0
for step in instructions:
    if i< 10:
        print(step)
    ship.read_instruction(step)
    if i< 10:
        print("Ship position: ", end = '\t\t')
        print(ship.position)
        print("Waypoint position: ", end = '\t')
        print(ship.waypoint_pos)
        print()
    i += 1
    ship.update_position()
    
ship.calculate_manhattan()
print(sum(ship.manhattan))

import matplotlib.pyplot as plt

plt.plot(ship.x_pos, ship.y_pos)
plt.show()