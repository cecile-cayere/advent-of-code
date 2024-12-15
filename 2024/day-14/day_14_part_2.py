import sys
sys.path.append('../advent-of-code')
from utils import *
from math import *

content = get_file_content('2024/day-14/input.txt')
content = split_string(content, "\n")

map = init_2_dim_list(101, 103)

vertical_half = ceil(101 / 2) - 1
horizontal_half = ceil(103 / 2) - 1

robots = []

for line in content:
    p, v = split_string(line, " ")
    p = split_string(p, "p=")[1]
    v = split_string(v, "v=")[1]

    py, px = split_string(p, ",")
    vy, vx = split_string(v, ",")
    px, py, vx, vy = int(px), int(py), int(vx), int(vy)
    robots.append({"p": [px, py], "v": [vx, vy]})

    map[px][py] = map[px][py] + 1

horizontal_lines = False
sec = 0
while not horizontal_lines:
    for robot in robots:
        px, py = robot["p"]
        vx, vy = robot["v"]

        if(px + vx >= len(map)):
            new_px = abs(vx - (len(map) - px))
        elif(px + vx < 0):
            new_px = abs((len(map)) + (vx + px))
        else:
            new_px = px + vx

        if(py + vy >= len(map[px])):
            new_py = abs(vy - (len(map[px]) - py))
        elif(py + vy < 0):
            new_py = abs((len(map[px])) + (vy + py))
        else:
            new_py = py + vy

        map[px][py] = map[px][py] - 1
        map[new_px][new_py] = map[new_px][new_py] + 1
        
        robot["p"] = [new_px, new_py]

    for line in map:
        counter = 0
        for point in line:
            if(point > 0):
                counter = counter + 1
            else:
                counter = 0

            if(counter == 10):
                horizontal_lines = True

    sec = sec + 1

for line in map:
    for point in line:
        if(point == 0):
            print(".", end=' ')
        else:
            print(point, end=' ')
    print()
print(sec)