import sys
sys.path.append('../advent-of-code')
from utils import *

content = get_file_content('2016/day-01/input.txt')
content = split_string(content, ", ")

current_position = [0, 0]
facing = "N"

for step in content:
    direction = step[0]
    blocks  = int(step[1:])

    if(direction == "R"):
        if(facing == "N"):
            facing = "E"
            current_position[1] = current_position[1] + blocks
        elif(facing == "E"):
            facing = "S"
            current_position[0] = current_position[0] - blocks
        elif(facing == "S"):
            facing = "O"
            current_position[1] = current_position[1] - blocks
        elif(facing == "O"):
            facing = "N"
            current_position[0] = current_position[0] + blocks
        else:
            print("Error!")

    elif(direction == "L"):
        if(facing == "N"):
            facing = "O"
            current_position[1] = current_position[1] - blocks
        elif(facing == "E"):
            facing = "N"
            current_position[0] = current_position[0] + blocks
        elif(facing == "S"):
            facing = "E"
            current_position[1] = current_position[1] + blocks
        elif(facing == "O"):
            facing = "S"
            current_position[0] = current_position[0] - blocks
        else:
            print("Error!")

    else:
        print("Error!")

print(get_distance_between_points([0, 0], current_position))