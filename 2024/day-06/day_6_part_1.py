import sys
sys.path.append('../advent-of-code')
from utils import *
import os
import time

content = get_file_content('2024/day-06/input.txt')
content = split_string(content, "\n")

map = init_2_dim_list(len(content), len(content[0]))
guard_position = [0, 0]

i = 0
for line in content:
    j = 0
    for char in line:
        if(char == "^"):
            guard_position = [i, j]

        map[i][j] = char
        j = j + 1
    i = i + 1

direction = "N"
is_out = False

while not is_out:
    if(direction == "N" and guard_position[0] - 1 >= 0 and (map[guard_position[0] - 1][guard_position[1]] == "." or map[guard_position[0] - 1][guard_position[1]] == "X")):
        map[guard_position[0] - 1][guard_position[1]] = "X"
        guard_position = [guard_position[0] - 1, guard_position[1]]

        if(guard_position[0] - 1 >= 0 and map[guard_position[0] - 1][guard_position[1]] == "#"):
           direction = "E"

    elif(direction == "E" and guard_position[1] + 1 < len(map[0]) and (map[guard_position[0]][guard_position[1] + 1] == "." or map[guard_position[0]][guard_position[1] + 1] == "X")):
        map[guard_position[0]][guard_position[1] + 1] = "X"
        guard_position = [guard_position[0], guard_position[1] + 1]

        if(guard_position[1] + 1 < len(map[0]) and map[guard_position[0]][guard_position[1] + 1] == "#"):
           direction = "S"

    elif(direction == "S" and guard_position[0] + 1 < len(map) and (map[guard_position[0] + 1][guard_position[1]] == "." or map[guard_position[0] + 1][guard_position[1]] == "X")):
        map[guard_position[0] + 1][guard_position[1]] = "X"
        guard_position = [guard_position[0] + 1, guard_position[1]]

        if(guard_position[0] + 1 < len(map) and map[guard_position[0] + 1][guard_position[1]] == "#"):
           direction = "W"
    
    elif(direction == "W" and guard_position[1] - 1 >= 0 and (map[guard_position[0]][guard_position[1] - 1] == "." or map[guard_position[0]][guard_position[1] - 1] == "X")):
        map[guard_position[0]][guard_position[1] - 1] = "X"
        guard_position = [guard_position[0], guard_position[1] - 1]

        if(guard_position[1] - 1 >= 0 and map[guard_position[0]][guard_position[1] - 1] == "#"):
           direction = "N"



    if ((direction == "N" and guard_position[0] - 1 < 0) or 
    (direction == "E" and guard_position[1] + 1 >= len(map[0])) or
    (direction == "S" and guard_position[0] + 1 >= len(map)) or
    (direction == "W" and guard_position[1] - 1 < 0)):
        is_out = True
    #os.system('cls')
    #print_map(map)
    #print()

count = 0
for line in map:
    for char in line:
        if(char == "X" or char == "^"):
            count = count + 1
print(count)
