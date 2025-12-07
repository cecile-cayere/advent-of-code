import sys
sys.path.append('../advent-of-code')
from utils import *

content = get_file_content('2025/day-07/input.txt')
content = split_string(content, "\n")

map = init_2_dim_list(len(content[0]), len(content))
values = init_2_dim_list(len(content[0]), len(content))

i = 0
start = [-1, -1]
for line in content:
    j = 0
    for char in line:
        if(char == "S"):
            start = [i, j]
            values[i][j] = 1
        map[i][j] = char
        j = j + 1
    i = i + 1

# Méthode récursive, ne fonctionne pas.
# def count_timelines(map, x, y):
#     if(x >= len(map) - 1):
#         return 1
    
#     if(map[x + 1][y] == "."):
#         return count_timelines(map, x + 1, y)
#     elif(map[x + 1][y] == "^"):
#         return count_timelines(map, x + 1, y - 1) + count_timelines(map, x + 1, y + 1)

# print(count_timelines(map, start[0], start[1]))

i = 0

while i < len(map) - 1:
    j = 0
    while j < len(map[0]):
        if (map[i][j] == "S" or map[i][j] == "|"):
            if(map[i + 1][j] == "." or map[i + 1][j] == "|"):
                map[i + 1][j] = "|"
                values[i + 1][j] = values[i + 1][j] + values[i][j]
            elif(map[i + 1][j] == "^"):
                map[i + 1][j - 1] = "|"
                map[i + 1][j + 1] = "|"
                values[i + 1][j] = values[i][j]
                values[i + 1][j - 1] = values[i + 1][j - 1] + values[i][j]
                values[i + 1][j + 1] = values[i + 1][j + 1] + values[i][j]
                
        j = j + 1
    i = i + 1

print(sum(values[-1]))