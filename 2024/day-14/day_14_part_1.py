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

sec = 100
while sec > 0:
    quadrant_1 = 0
    quadrant_2 = 0
    quadrant_3 = 0
    quadrant_4 = 0
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

        if(new_px < horizontal_half and new_py < vertical_half):
            quadrant_1 = quadrant_1 + 1
        elif(new_px < horizontal_half and new_py > vertical_half):
            quadrant_2 = quadrant_2 + 1
        elif(new_px > horizontal_half and new_py < vertical_half):
            quadrant_3 = quadrant_3 + 1
        elif(new_px > horizontal_half and new_py > vertical_half):
            quadrant_4 = quadrant_4 + 1
    sec = sec - 1

print(quadrant_1 * quadrant_2 * quadrant_3 * quadrant_4)