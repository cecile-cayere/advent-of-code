import sys
sys.path.append('../advent-of-code')
from utils import *
import copy

content = get_file_content('2016/day-01/input.txt')
content = split_string(content, ", ")

def get_distance_between(point_1, point_2):
    return(abs(point_2[0] - point_1[0]) + abs(point_2[1] - point_1[1]))


current_position = [0, 0]
locations_list = []
facing = "N"

for step in content:
    direction = step[0]
    blocks  = int(step[1:])

    if((direction == "R") and (facing == "N")) or ((direction == "L") and (facing == "S")):
        facing = "E"
    elif((direction == "R") and (facing == "E")) or ((direction == "L") and (facing == "O")):
        facing = "S"
    elif((direction == "R") and (facing == "S")) or ((direction == "L") and (facing == "N")):
        facing = "O"
    elif((direction == "R") and (facing == "O")) or ((direction == "L") and (facing == "E")):
        facing = "N"
    else:
        print("Error!")

    i = 0
    while i < blocks:
        if(facing == "E"):
            current_position[1] = current_position[1] + 1
        elif(facing == "S"):
            current_position[0] = current_position[0] - 1
        elif(facing == "O"):
            current_position[1] = current_position[1] - 1
        elif(facing == "N"):
            current_position[0] = current_position[0] + 1
        else:
            print("Error!")

        if(current_position in locations_list):
            print(get_distance_between([0, 0], current_position))
            exit(1)

        else:
            locations_list.append(copy.deepcopy(current_position))

        i = i + 1
