import sys
sys.path.append('../advent-of-code')
from utils import *

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
                map[i].append(char)
                if(char == "@"):
                    robot = [i, j]
                j = j + 1
            i = i + 1

        else:
            for char in line:
                movements.append(char)

for movement in movements:
    x, y = robot
    if(movement == "^" and map[x - 1][y] != "#"):
        if(map[x - 1][y] == "."):
            map[x][y] = "."
            map[x - 1][y] = "@"
            robot = [x - 1, y]
        else:
            boxes_end = False
            i = x - 1
            while not boxes_end:
                if(map[i][y] != "O"):
                    if(map[i][y] == "."):
                        map[x][y] = "."
                        map[x - 1][y] = "@"
                        robot = [x - 1, y]
                        map[i][y] = "O"
                    boxes_end = True
                i = i - 1


    elif(movement == ">" and map[x][y + 1] != "#"):
        if(map[x][y + 1] == "."):
            map[x][y] = "."
            map[x][y + 1] = "@"
            robot = [x, y + 1]
        else:
            boxes_end = False
            j = y + 1
            while not boxes_end:
                if(map[x][j] != "O"):
                    if(map[x][j] == "."):
                        map[x][y] = "."
                        map[x][y + 1] = "@"
                        robot = [x, y + 1]
                        map[x][j] = "O"
                    boxes_end = True
                j = j + 1

    elif(movement == "v" and map[x + 1][y] != "#"):
        if(map[x + 1][y] == "."):
            map[x][y] = "."
            map[x + 1][y] = "@"
            robot = [x + 1, y]
        else:
            boxes_end = False
            i = x + 1
            while not boxes_end:
                if(map[i][y] != "O"):
                    if(map[i][y] == "."):
                        map[x][y] = "."
                        map[x + 1][y] = "@"
                        robot = [x + 1, y]
                        map[i][y] = "O"
                    boxes_end = True
                i = i + 1

    elif(movement == "<" and map[x][y - 1] != "#"):
        if(map[x][y - 1] == "."):
            map[x][y] = "."
            map[x][y - 1] = "@"
            robot = [x, y - 1]
        else:
            boxes_end = False
            j = y - 1
            while not boxes_end:
                if(map[x][j] != "O"):
                    if(map[x][j] == "."):
                        map[x][y] = "."
                        map[x][y - 1] = "@"
                        robot = [x, y - 1]
                        map[x][j] = "O"
                    boxes_end = True
                j = j - 1

sum = 0
i = 0
for line in map:
    j = 0
    for point in line:
        if(point == "O"):
            sum = sum + ((100 * i) + j)
        j = j + 1
    i = i + 1
print(sum)