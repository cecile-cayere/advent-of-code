import sys
sys.path.append('../advent-of-code')
from utils import *

def get_trails(map, current_position):
    x, y = current_position

    if(map[x][y] == 9):
        return 1
    
    rating = 0

    if(x - 1 >= 0           and map[x][y] + 1 == map[x - 1][y]):
        rating = rating + get_trails(map, [x - 1, y])
    if(y + 1 < len(map[x])  and map[x][y] + 1 == map[x][y + 1]):
        rating = rating + get_trails(map, [x, y + 1])
    if(x + 1 < len(map)     and map[x][y] + 1 == map[x + 1][y]):
        rating = rating + get_trails(map, [x + 1, y])
    if(y - 1 >= 0           and map[x][y] + 1 == map[x][y - 1]):
        rating = rating + get_trails(map, [x, y - 1])

    return rating

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
    total_score = total_score + get_trails(map, trailhead)

print(total_score)