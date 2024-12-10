import sys
sys.path.append('../advent-of-code')
from utils import *

summits = []

def get_trails(map, current_position):
    x, y = current_position

    if(map[x][y] == 9):
        if(current_position not in summits):
            summits.append(current_position)
            return 1
        else: 
            return 0
    
    trailhead_score = 0

    if(x - 1 >= 0           and map[x][y] + 1 == map[x - 1][y]):
        trailhead_score = trailhead_score + get_trails(map, [x - 1, y])
    if(y + 1 < len(map[x])  and map[x][y] + 1 == map[x][y + 1]):
        trailhead_score = trailhead_score + get_trails(map, [x, y + 1])
    if(x + 1 < len(map)     and map[x][y] + 1 == map[x + 1][y]):
        trailhead_score = trailhead_score + get_trails(map, [x + 1, y])
    if(y - 1 >= 0           and map[x][y] + 1 == map[x][y - 1]):
        trailhead_score = trailhead_score + get_trails(map, [x, y - 1])

    return trailhead_score

content = get_file_content('2024/day-10/input.txt')
content = split_string(content, "\n")

map = init_2_dim_list(len(content), len(content[0]))
trailheads = []

i = 0
for line in content:
    j = 0
    for char in line:
        map[i][j] = int(char)
        if(char == "0"):
            trailheads.append([i, j])
        j = j + 1
    i = i + 1

total_score = 0

for trailhead in trailheads:
    summits = []
    score = get_trails(map, trailhead)
    total_score = total_score + score

print(total_score)