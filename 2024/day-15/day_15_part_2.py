import sys
sys.path.append('../advent-of-code')
from utils import *
import copy

def can_move(map, tile, direction):
    x, y = tile
    if(direction == "^"):
        if(map[x - 1][y] == "." or map[x - 1][y] == "[" or map[x - 1][y] == "]"):
            return True
        else:
            return False
    elif(direction == ">"):
        if(map[x][y + 1] == "." or map[x][y + 1] == "[" or map[x][y + 1] == "]"):
            return True
        else:
            return False
    elif(direction == "v"):
        if(map[x + 1][y] == "." or map[x + 1][y] == "[" or map[x + 1][y] == "]"):
            return True
        else:
            return False
    else:
        if(map[x][y - 1] == "." or map[x][y - 1] == "[" or map[x][y - 1] == "]"):
            return True
        else:
            return False

content = get_file_content('2024/day-15/input.txt')
content = split_string(content, "\n")

map = []
movements = []
robot = []
switch = False
i = 0
for line in content:
    if(line == ""):
        switch = True

    else:
        if(switch == False):
            map.append([])
            j = 0
            for char in line:
                if(char == "."):
                    map[i].append(char)
                    map[i].append(".")
                    j = j + 2
                if(char == "#"):
                    map[i].append(char)
                    map[i].append("#")
                    j = j + 2
                if(char == "O"):
                    map[i].append("[")
                    map[i].append("]")
                    j = j + 2
                elif(char == "@"):
                    map[i].append(char)
                    map[i].append(".")
                    robot = [i, j]
                    j = j + 2
            i = i + 1

        else:
            for char in line:
                movements.append(char)

for movement in movements:
    x, y = robot
    tiles_moving = []
    tiles_moving.append(robot)

    if(can_move(map, robot, movement)):
        if(movement == "^"):
            previous_tiles_moving = []
            no_move = False

            while previous_tiles_moving != tiles_moving:
                previous_tiles_moving = copy.deepcopy(tiles_moving)
                for tile_moving in previous_tiles_moving:
                    x, y = tile_moving
                    if(map[x - 1][y] == "["):
                        if(can_move(map, [x - 1, y], movement)):
                            if([x - 1, y] not in tiles_moving): tiles_moving.append([x - 1, y])
                        else: no_move = True
                        if(can_move(map, [x - 1, y + 1], movement)):
                            if([x - 1, y + 1] not in tiles_moving): tiles_moving.append([x - 1, y + 1])
                        else: no_move = True
                    elif(map[x - 1][y] == "]"):
                        if(can_move(map, [x - 1, y], movement)):
                            if([x - 1, y] not in tiles_moving): tiles_moving.append([x - 1, y])
                        else: no_move = True
                        if(can_move(map, [x - 1, y - 1], movement)):
                            if([x - 1, y - 1] not in tiles_moving): tiles_moving.append([x - 1, y - 1])
                        else: no_move = True
                    elif(map[x - 1][y] == "#"):
                        no_move = True

            if(not no_move):
                tmp_map = copy.deepcopy(map)
                for tile_moving in tiles_moving:
                    x, y = tile_moving
                    tmp_map[x - 1][y] = map[x][y]
                    if(map[x][y] == "@"):
                        robot = [x - 1, y]
                    if([x + 1, y] in tiles_moving):
                        tmp_map[x][y] = map[x + 1][y]
                    else:
                        tmp_map[x][y] = "."

                map = copy.deepcopy(tmp_map)

        elif(movement == ">"):
            previous_tiles_moving = []
            no_move = False

            while previous_tiles_moving != tiles_moving:
                previous_tiles_moving = copy.deepcopy(tiles_moving)
                for tile_moving in previous_tiles_moving:
                    x, y = tile_moving
                    if(map[x][y + 1] == "["):
                        if(can_move(map, [x, y + 1], movement)):
                            if([x, y + 1] not in tiles_moving): tiles_moving.append([x, y + 1])
                        else: no_move = True
                        if(can_move(map, [x, y + 2], movement)):
                            if([x, y + 2] not in tiles_moving): tiles_moving.append([x, y + 2])
                        else: no_move = True
                    elif(map[x][y + 1] == "#"):
                        no_move = True

            if(not no_move):
                tmp_map = copy.deepcopy(map)
                for tile_moving in tiles_moving:
                    x, y = tile_moving
                    tmp_map[x][y + 1] = map[x][y]
                    if(map[x][y] == "@"):
                        robot = [x, y + 1]
                    if([x, y - 1] in tiles_moving):
                        tmp_map[x][y] = map[x][y - 1]
                    else:
                        tmp_map[x][y] = "."

                map = copy.deepcopy(tmp_map)

        elif(movement == "v"):
            previous_tiles_moving = []
            no_move = False

            while previous_tiles_moving != tiles_moving:
                previous_tiles_moving = copy.deepcopy(tiles_moving)
                for tile_moving in previous_tiles_moving:
                    x, y = tile_moving
                    if(map[x + 1][y] == "["):
                        if(can_move(map, [x + 1, y], movement)):
                            if([x + 1, y] not in tiles_moving): tiles_moving.append([x + 1, y])
                        else: no_move = True
                        if(can_move(map, [x + 1, y + 1], movement)):
                            if([x + 1, y + 1] not in tiles_moving): tiles_moving.append([x + 1, y + 1])
                        else: no_move = True
                    elif(map[x + 1][y] == "]"):
                        if(can_move(map, [x + 1, y], movement)):
                            if([x + 1, y] not in tiles_moving): tiles_moving.append([x + 1, y])
                        else: no_move = True
                        if(can_move(map, [x + 1, y - 1], movement)):
                            if([x + 1, y - 1] not in tiles_moving): tiles_moving.append([x + 1, y - 1])
                        else: no_move = True
                    elif(map[x + 1][y] == "#"): 
                        no_move = True

            if(not no_move):
                tmp_map = copy.deepcopy(map)
                for tile_moving in tiles_moving:
                    x, y = tile_moving
                    tmp_map[x + 1][y] = map[x][y]
                    if(map[x][y] == "@"):
                        robot = [x + 1, y]
                    if([x - 1, y] in tiles_moving):
                        tmp_map[x][y] = map[x - 1][y]
                    else:
                        tmp_map[x][y] = "."

                map = copy.deepcopy(tmp_map)
        
        
        elif(movement == "<"):
            previous_tiles_moving = []
            no_move = False

            while previous_tiles_moving != tiles_moving:
                previous_tiles_moving = copy.deepcopy(tiles_moving)
                for tile_moving in previous_tiles_moving:
                    x, y = tile_moving
                    if(map[x][y - 1] == "]"):
                        if(can_move(map, [x, y - 1], movement)):
                            if([x, y - 1] not in tiles_moving): tiles_moving.append([x, y - 1])
                        else: no_move = True
                        if(can_move(map, [x, y - 2], movement)):
                            if([x, y - 2] not in tiles_moving): tiles_moving.append([x, y - 2])
                        else: no_move = True
                    elif(map[x][y - 1] == "#"): 
                        no_move = True

            if(not no_move):
                tmp_map = copy.deepcopy(map)
                for tile_moving in tiles_moving:
                    x, y = tile_moving
                    tmp_map[x][y - 1] = map[x][y]
                    if(map[x][y] == "@"):
                        robot = [x, y - 1]
                    if([x, y + 1] in tiles_moving):
                        tmp_map[x][y] = map[x][y + 1]
                    else:
                        tmp_map[x][y] = "."

                map = copy.deepcopy(tmp_map)
        
print_map(map)

sum = 0
i = 0
for line in map:
    j = 0
    for point in line:
        if(point == "["):
            sum = sum + ((100 * i) + j)
        j = j + 1
    i = i + 1

print(sum)