import sys
sys.path.append('../advent-of-code')
from utils import *
import os
import copy

def is_stuck(map, guard_position):
    direction_symbols = ["↑", "→", "↓", "←"]
    direction = "N"

    while 1:
        if(direction == "N"):
            x = guard_position[0] - 1
            y = guard_position[1]
            if(x >= 0):
                if(map[x][y] == "↑"):
                    return True
                elif(map[x][y] == "#"):
                    direction = "E"
                elif(map[x][y] == "." or map[x][y] in direction_symbols):
                    map[x][y] = "↑"
                    guard_position = [x, y]
            else:
                return False
            
        elif(direction == "E"):
            x = guard_position[0]
            y = guard_position[1] + 1
            if(y < len(map[0])):
                if(map[x][y] == "→"):
                    return True
                elif(map[x][y] == "#"):
                    direction = "S"
                elif(map[x][y] == "." or map[x][y] in direction_symbols):
                    map[x][y] = "→"
                    guard_position = [x, y]
            else:
                return False
            
        elif(direction == "S"):
            x = guard_position[0] + 1
            y = guard_position[1]
            if(x < len(map)):
                if(map[x][y] == "↓"):
                    return True
                elif(map[x][y] == "#"):
                    direction = "W"
                elif(map[x][y] == "." or map[x][y] in direction_symbols):
                    map[x][y] = "↓"
                    guard_position = [x, y]
            else:
                return False
            
        else:
            x = guard_position[0]
            y = guard_position[1] - 1
            if(y >= 0):
                if(map[x][y] == "←"):
                    return True
                elif(map[x][y] == "#"):
                    direction = "N"
                elif(map[x][y] == "." or map[x][y] in direction_symbols):
                    map[x][y] = "←"
                    guard_position = [x, y]
            else:
                return False
               
content = get_file_content('2024/day-06/input.txt')
content = split_string(content, "\n")

map = init_2_dim_list(len(content), len(content[0]))
guard_position = [0, 0]

i = 0
for line in content:
    j = 0
    for char in line:
        map[i][j] = char
        if(char == "^"):
            map[i][j] = "↑"
            guard_position = [i, j]

        j = j + 1
    i = i + 1

count = 0
i = 0
for line in content:
    j = 0
    for char in line:
        if(map[i][j] == "."):
            map_copy = copy.deepcopy(map)
            map_copy[i][j] = "#"
            
            if(is_stuck(map_copy, guard_position)):
                count = count + 1
        j = j + 1
    i = i + 1
print(count)

