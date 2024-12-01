import sys
sys.path.append('../advent-of-code')
from utils import *

content = get_file_content('2016/day-01/input.txt')
content = split_string(content, ", ")

def get_distance_between(point_1, point_2):
    return(abs(point_2[0] - point_1[0]) + abs(point_2[1] - point_1[1]))

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

print(get_distance_between([0, 0], current_position))